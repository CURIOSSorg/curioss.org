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

Site content driven by YAML lives in [`data/`](data/) — funding opportunities or talks. Each file has a JSON Schema in
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
```

A clean run prints `ok -- validation done`. Any other output is an error to fix.
