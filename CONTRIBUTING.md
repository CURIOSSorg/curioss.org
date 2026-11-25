# Contributing
Contributions to this repo are welcome. Please follow the following guidelines:

## Forking

* Please fork the project using the fork button at the top of this page ☝️
* Make your proposed changes inside your fork.
* Test your build locally.
* Commit to your fork.
* Follow the GitHub Guidelines on creating a pull request.
* Please be as descriptive as necessary in your PR.

## Editing data files

Site content driven by YAML lives in [`data/`](data/) — funding opportunities, talks, or members. Each file has a JSON Schema in
[`data/schemas/`](data/schemas/) that lists the required and allowed fields, the
expected types, and the formats (dates, URLs, image paths). The schemas are the
source of truth for what a valid entry looks like.

Every pull request that touches `data/` runs the **Lint data files** check.
If it fails, open the check log to see exactly which file, which entry, and
which field is wrong — for example:

```
data/funding-opportunities.yml::$.opportunities[6].posted: '2026-13-01' is not a 'date'
data/funding-opportunities.yml::$.opportunities[7]: 'url' is a required property
```

The path after `::` points to the entry (`$.opportunities[6]` is the 7th item)
and the field that needs fixing.

### Running the check locally

You don't need to run checks locally - the GitHub action will flag any PRs, which is another way to check. If you do want to test locally, you'll need Python 3.

```bash
pip install check-jsonschema
check-jsonschema --schemafile data/schemas/funding-opportunities.schema.json data/funding-opportunities.yml
check-jsonschema --schemafile data/schemas/talks.schema.json              data/talks.yml
check-jsonschema --schemafile data/schemas/members.schema.json            data/members.yml
```

A clean run prints `ok -- validation done`. Any other output is an error to fix.

## Adding a member

Add the institution to [`data/members.yml`](data/members.yml), and put its logo in `static/images/about/logos/`. If it has a page in the [CURIOSS Academic Map](https://curioss.org/academic-map/intro.html), set `mapPage` too, and the map will show the logo on that page the next time it builds.

## Crediting news authors

List a post's authors at the top of the post file, between the `---` lines, in the order they should appear. You only need to edit that one file. Copy this and fill it in:

```yaml
authors:
  - name: "Jane Doe"
    orcid: "0000-0002-1825-0097"
    affiliations: ["Example University"]
    url: "https://example.org"
  - name: "John Smith"
```

Only `name` is required. Delete any other line you don't need. `url` is one website of the author's choice, linked from their name. Keep the field names in lowercase, and the spaces at the start of each line as shown. The page already shows the post's title, so don't repeat it as a heading in the post.

On each pull request, the **Check news authors** check compares new and edited posts with the others. It fails if a name looks like a misspelling of an existing author (such as "J. Doe" for "Jane Doe"), if an ORCID iD is invalid or doesn't match the name, or if the fields are written incorrectly. It warns, without failing, if a post has no authors or if someone's affiliations or website differ between posts, which can be correct. Open the check or the **Files changed** tab to see what to fix. If two different people really do have similar names, add both ORCID iDs, or a maintainer can merge anyway.

[`data/authors.yml`](data/authors.yml) is a registry of all authors. You don't need to edit it: once the check passes, a workflow rebuilds it and commits it to your pull request. If you're also editing the branch on your own computer, pull that commit before pushing again. Pull requests from forks are skipped, and the next pull request from this repository adds their authors. If two open pull requests conflict in this file, keep either version, because it's rebuilt from the posts.

## Generated folders

Two folders are built in other repositories and pushed here on every deploy. Don't edit them by hand, because the next deploy overwrites them. Make the change in the source repository instead.

* `static/patterns/` comes from [CURIOSSorg/curioss-patterns](https://github.com/CURIOSSorg/curioss-patterns).
* `static/academic-map/` comes from [CURIOSSorg/academic-map](https://github.com/CURIOSSorg/academic-map).
