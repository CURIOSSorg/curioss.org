#!/usr/bin/env python3
"""Warn about H1 headings in news posts added or edited since a git ref.

    headings.py --base <git ref>

A post's title is its page's only H1, so headings in the post should start at ##.
"""

import argparse
import re

from authors import changed_posts, report

MESSAGE = (
    "This is a level 1 heading, which is bigger than the post's title. "
    "Change it to `##` or lower, and move any subheadings under it down a level too"
)


def h1_lines(text):
    """Return the line numbers of H1 headings, skipping front matter and code blocks."""
    lines = text.splitlines()
    start = 0
    if lines and lines[0].rstrip() == "---":
        start = next((i + 1 for i in range(1, len(lines)) if lines[i].rstrip() == "---"), 0)

    found = []
    fence = None
    previous = ""
    for number, line in enumerate(lines[start:], start + 1):
        marker = re.match(r" {0,3}(`{3,}|~{3,})(.*)", line)
        if fence:
            # A block closes with at least as many of the same character, and nothing else.
            if marker and marker[1].startswith(fence) and not marker[2].strip():
                fence = None
        elif marker:
            fence = marker[1]
            previous = ""
        else:
            if re.match(r" {0,3}#(\s|$)", line) or re.search(r"<h1[\s>]", line, re.I):
                found.append(number)
            # A line of = signs makes the line of text above it an H1.
            elif previous.strip() and re.match(r" {0,3}=+\s*$", line):
                found.append(number - 1)
            previous = line
    return found


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base", required=True)
    args = parser.parse_args()

    count = 0
    for path in changed_posts(args.base):
        if path.name == "_index.md" or not path.exists():
            continue
        for number in h1_lines(path.read_text(encoding="utf-8-sig")):
            report("warning", path, MESSAGE, number)
            count += 1
    print(f"Found {count} level 1 heading(s) to change.")
