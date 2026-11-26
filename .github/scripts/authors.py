#!/usr/bin/env python3
"""News post authors: check them on pull requests, and build the registry from them.

    authors.py check --base <git ref>   check posts added or edited since <git ref>
    authors.py build                    rewrite data/authors.yml from all posts

The posts are the source of truth. data/authors.yml is generated from them, and
the site uses it to fill in any details that a post leaves out.
"""

import argparse
import difflib
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

NEWS = Path("content/news")
REGISTRY = Path("data/authors.yml")
FIELDS = {"name", "orcid", "affiliations", "url"}
HEADER = """\
# GENERATED FILE: do not edit. It's rebuilt from the news posts on each pull request.
# Posts that give only an author's name get the rest of their details from this file.
# To change a detail, write it in the front matter of a post in content/news/.
# Each detail here comes from the newest post that states it.
"""


def report(level, path, message, line=1):
    """Print a GitHub Actions annotation, shown on the pull request."""
    def escape(text):
        return str(text).replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")

    prop = escape(path).replace(":", "%3A").replace(",", "%2C")
    print(f"::{level} file={prop},line={line}::{escape(message)}")


def line_of(path, text):
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if text in line:
            return number
    return 1


def valid_orcid(orcid):
    """Check the shape and the final check digit (ISO 7064 mod 11-2)."""
    if not re.fullmatch(r"\d{4}-\d{4}-\d{4}-\d{3}[\dX]", orcid):
        return False
    digits = orcid.replace("-", "")
    total = 0
    for digit in digits[:-1]:
        total = (total + int(digit)) * 2
    check = (12 - total % 11) % 11
    return digits[-1] == ("X" if check == 10 else str(check))


def front_matter(path):
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", path.read_text(encoding="utf-8-sig"), re.S)
    if not match:
        return {}
    data = yaml.safe_load(match.group(1)) or {}
    # Hugo ignores the case of front matter keys, so do the same.
    return {str(key).lower(): value for key, value in data.items()}


def without_blanks(value):
    """Drop empty fields, such as those left over from the new post template."""
    blank = (None, "", [], {})
    if isinstance(value, dict):
        cleaned = {str(key): without_blanks(item) for key, item in value.items()}
        return {key: item for key, item in cleaned.items() if item not in blank}
    if isinstance(value, list):
        return [item for item in map(without_blanks, value) if item not in blank]
    if isinstance(value, str):
        return value.strip()
    return value


def read_post(path):
    """Return (date, authors, problems) for one post."""
    try:
        meta = front_matter(path)
    except yaml.YAMLError as error:
        return "", [], [(1, f"The front matter isn't valid YAML: {error}")]

    date = str(meta.get("date") or "")
    raw = without_blanks(meta.get("authors"))
    if raw in (None, "", [], {}):
        return date, [], []
    if not isinstance(raw, list):
        return date, [], [(line_of(path, "authors"), "`authors` must be a list, with each author starting `- name:`")]

    authors, problems = [], []
    for entry in raw:
        if not isinstance(entry, dict):
            problems.append((line_of(path, str(entry)), f"Write this author as `- name: \"{entry}\"`"))
            continue
        # Hugo is case-sensitive about these keys, so `Name:` is an unknown field.
        name = str(entry.get("name", "")).strip()
        if not name:
            problems.append((line_of(path, "authors"), "Every author needs a `name`"))
            continue
        line = line_of(path, name)
        for key in sorted(set(entry) - FIELDS):
            problems.append((line, f"{name}: unknown field `{key}`. Use name, orcid, affiliations or url"))

        author = {"name": name, "line": line}
        if "orcid" in entry:
            orcid = re.sub(r"^https?://orcid\.org/", "", str(entry["orcid"]).strip()).rstrip("/")
            if valid_orcid(orcid):
                author["orcid"] = orcid
            else:
                problems.append((line, f"{name}: `{orcid}` isn't a valid ORCID iD. Check it for typos"))
        if "affiliations" in entry:
            value = entry["affiliations"]
            value = value if isinstance(value, list) else [value]
            if all(isinstance(item, str) and item.strip() for item in value):
                author["affiliations"] = [item.strip() for item in value]
            else:
                problems.append((line, f"{name}: `affiliations` must be a list of names"))
        if "url" in entry:
            url = str(entry["url"]).strip()
            if re.match(r"https?://\S+$", url):
                author["url"] = url
            else:
                problems.append((line, f"{name}: `url` must be a single link starting with http:// or https://"))
        authors.append(author)
    return date, authors, problems


def all_posts():
    return {path: read_post(path) for path in sorted(NEWS.rglob("*.md")) if path.name != "_index.md"}


def oldest_first(posts):
    return sorted(posts.items(), key=lambda item: (item[1][0], str(item[0])))


def new_defaults(path, author, posts):
    """Warn if this post changes a default that other posts are relying on."""
    entries = [
        (other_path, other)
        for other_path, (_, authors, _) in oldest_first(posts)
        for other in authors
        if other["name"] == author["name"]
    ]
    messages = []
    for field in ("affiliations", "url"):
        stated = [(other_path, other[field]) for other_path, other in entries if field in other]
        # Only the newest post stating a field sets its default.
        if field not in author or stated[-1][0] != path:
            continue
        before = [value for other_path, value in stated if other_path != path]
        relying = [str(other_path) for other_path, other in entries if field not in other]
        if before and relying and before[-1] != author[field]:
            messages.append(
                f"This changes the default {field} for {author['name']} from {before[-1]} to {author[field]}. "
                f"These posts don't state their own, so they'll change too: {', '.join(relying)}. "
                f"To keep the old value on them, add it to each one"
            )
    return messages


def plain(name):
    """A name without case, accents or punctuation."""
    text = unicodedata.normalize("NFKD", name.casefold())
    text = "".join(char for char in text if not unicodedata.combining(char))
    return " ".join(re.findall(r"\w+", text))


def looks_alike(first, second):
    a, b = plain(first).split(), plain(second).split()
    if not a or not b:
        return False
    # Same family name, and the given names match or one is an initial
    # (V. Louvet / Violaine Louvet, Daniel Katz / Daniel S. Katz).
    if a[-1] == b[-1]:
        x, y = a[0], b[0]
        if x == y or ((len(x) == 1 or len(y) == 1) and x[0] == y[0]):
            return True
    # Family name written first, or a likely typo.
    return sorted(a) == sorted(b) or difflib.SequenceMatcher(None, " ".join(a), " ".join(b)).ratio() >= 0.85


def compare(new, old):
    """Return (level, message) pairs for an author compared with one in another post."""
    orcids = (new.get("orcid"), old.get("orcid"))
    if new["name"] != old["name"]:
        if all(orcids) and orcids[0] == orcids[1]:
            return [("error", f"ORCID iD {orcids[0]} belongs to \"{old['name']}\" elsewhere, but is \"{new['name']}\" here")]
        # Different ORCID iDs mean these are different people.
        if not all(orcids) and looks_alike(new["name"], old["name"]):
            return [("error", f"\"{new['name']}\" looks like \"{old['name']}\". If they're the same person, spell the name the same way")]
        return []

    found = []
    if all(orcids) and orcids[0] != orcids[1]:
        found.append(("error", f"{new['name']} has ORCID iD {orcids[0]} here, but {orcids[1]}"))
    for field in ("url", "affiliations"):
        if field in new and field in old and new[field] != old[field]:
            found.append(("warning", f"{new['name']} has different {field} here ({new[field]}) than ({old[field]})"))
    return found


def changed_posts(base):
    output = subprocess.run(
        ["git", "diff", "--name-only", "-z", "--diff-filter=AMR", f"{base}...HEAD", "--", str(NEWS)],
        check=True, capture_output=True, text=True,
    ).stdout
    return [Path(name) for name in output.split("\0") if name.endswith(".md")]


def check(base):
    posts = all_posts()
    changed = [path for path in changed_posts(base) if path in posts]
    errors = 0
    checked = set()
    for path in changed:
        _, authors, problems = posts[path]
        for line, message in problems:
            report("error", path, message, line)
            errors += 1
        if not authors and not problems:
            report("warning", path, "This post doesn't list any authors")

        checked.add(path)
        for author in authors:
            for message in new_defaults(path, author, posts):
                report("warning", path, message, author["line"])
            seen = set()
            for other_path, (_, others, _) in posts.items():
                # Skip posts already checked, so each pair is reported once.
                if other_path in checked:
                    continue
                for other in others:
                    for level, message in compare(author, other):
                        if (level, message) in seen:
                            continue
                        seen.add((level, message))
                        report(level, path, f"{message} (see {other_path})", author["line"])
                        errors += level == "error"

    print(f"Checked {len(changed)} changed post(s): {errors} problem(s) to fix.")
    return 1 if errors else 0


def build():
    registry = {}
    # Oldest first, so that the newest post's details win.
    for path, (_, authors, problems) in oldest_first(all_posts()):
        for line, message in problems:
            report("warning", path, message, line)
        for author in authors:
            entry = registry.setdefault(author["name"], {"name": author["name"]})
            entry.update({key: author[key] for key in ("orcid", "affiliations", "url") if key in author})
            entry.setdefault("posts", []).append(path.as_posix())

    entries = sorted(registry.values(), key=lambda entry: plain(entry["name"]))
    ordered = [{key: entry[key] for key in ("name", "orcid", "affiliations", "url", "posts") if key in entry} for entry in entries]
    body = yaml.safe_dump({"authors": ordered}, allow_unicode=True, sort_keys=False, width=1000)
    REGISTRY.write_text(HEADER + "\n" + body, encoding="utf-8")
    print(f"Wrote {len(ordered)} author(s) to {REGISTRY}.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check").add_argument("--base", required=True)
    commands.add_parser("build")
    args = parser.parse_args()
    sys.exit(check(args.base) if args.command == "check" else build())
