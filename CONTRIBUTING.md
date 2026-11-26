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

## Adding a news post

**[Start a new news post](https://github.com/CURIOSSorg/curioss.org/new/main/content/news?filename=new-post.md&value=---%0Atitle%3A%20%22%22%0Adate%3A%20%20%23%20today%2C%20written%20like%202026-01-31%0Adescription%3A%20%22%22%20%20%23%20one%20short%20line%2C%20shown%20on%20the%20News%20page%0Aimage%3A%20%22%22%20%20%23%20such%20as%20%22%2Fimages%2Fnews%2Fmy-post.png%22%0Aauthors%3A%20%20%23%20for%20someone%20already%20in%20data%2Fauthors.yml%2C%20just%20fill%20in%20name.%20To%20add%20an%20author%2C%20copy%20all%20four%20lines%0A%20%20-%20name%3A%20%22%22%0A%20%20%20%20orcid%3A%20%22%22%0A%20%20%20%20affiliations%3A%20%5B%22%22%5D%0A%20%20%20%20url%3A%20%22%22%0A---%0A%0AWrite%20the%20post%20here.%20Don%27t%20repeat%20the%20title%20as%20a%20heading.%0A)**. This opens GitHub's editor with the fields every post needs, including the author fields.

1. Replace `new-post.md` in the filename box with a short name for your post, ending in `.md`.
2. Fill in the fields between the `---` lines, and write the post below them. Fill in `title` and `date`. See [Crediting news authors](#crediting-news-authors) for the author fields.
3. Select **Commit changes**, choose **Create a new branch for this commit and start a pull request**, and open the pull request.

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

**If someone is already in the [author registry](data/authors.yml), you only need their name**, spelled the same way. Their ORCID iD, affiliations and website are filled in from the registry:

```yaml
authors:
  - name: "Ciara Flanagan"
```

If a post states one of these details, the post shows its own version instead.

Only `name` is required for each author. You can leave any other field empty or delete its line; if the registry has that detail, it's filled in. An author with every field empty, including the name, is ignored. `url` is one website of the author's choice, linked from their name. Keep the field names in lowercase, and the spaces at the start of each line as shown. The page already shows the post's title, so don't repeat it as a heading in the post. Start section headings at `##`, and use `###` for subsections. Don't use `#`: it's the level for the title, so it shows up bigger than the title. The pull request check warns you if you do.

On each pull request, the **Check news posts** check compares new and edited posts with the others. It fails if a name looks like a misspelling of an existing author (such as "J. Doe" for "Jane Doe"), if an ORCID iD is invalid or doesn't match the name, or if the fields are written incorrectly. It warns, without failing, if a post uses a `#` heading (change it to `##` or lower), if a post has no authors or if someone's affiliations or website differ between posts, which can be correct. Open the check or the **Files changed** tab to see what to fix. If two different people really do have similar names, add both ORCID iDs, or a maintainer can merge anyway.

[`data/authors.yml`](data/authors.yml) is a registry of all authors. Each detail comes from the newest post, by date, that states it. You don't need to edit it: once the check passes, a workflow rebuilds it and commits it to your pull request. If you're also editing the branch on your own computer, pull that commit before pushing again. Pull requests from forks are skipped, and the next pull request from this repository adds their authors. If two open pull requests conflict in this file, keep either version, because it's rebuilt from the posts.

### When someone's details change

For example, if an author changes affiliation:

1. Add the old affiliation to any of their earlier posts that give no affiliation, so those posts keep it. Posts that already state one don't need changing.
2. Write the new affiliation in their next post. It becomes the default for later posts that give only their name.

If a new default would change earlier posts, the check warns you and lists them. Leaving a field empty means "use the registry", so a post can't show no affiliation for someone who has one there.

## The full-text news feed and Rogue Scholar

[`/news/atom.xml`](https://curioss.org/news/atom.xml) is an Atom feed with the full text of every news post, made so that [Rogue Scholar](https://rogue-scholar.org/) can archive the posts and make them citable. It builds itself from the posts, so there's nothing extra to edit. It names each author, with their ORCID iD if there is one, and otherwise their website. It doesn't include affiliations.

When you write a post, keep in mind what [Rogue Scholar asks for](https://rogue-scholar.org/faq):

* **License:** the feed offers every post under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), like the rest of the site. Make sure the authors agree, and that anything copied from elsewhere allows it.
* **Authors:** credit the people who wrote the post, and add their ORCID iDs if they have them.
* **AI:** posts must be written and approved by people. Posts primarily or entirely generated by an author using AI aren't accepted. If an author used an LLM to help with their writing, they need to say so in the post.

## Generated folders

Two folders are built in other repositories and pushed here on every deploy. Don't edit them by hand, because the next deploy overwrites them. Make the change in the source repository instead.

* `static/patterns/` comes from [CURIOSSorg/curioss-patterns](https://github.com/CURIOSSorg/curioss-patterns).
* `static/academic-map/` comes from [CURIOSSorg/academic-map](https://github.com/CURIOSSorg/academic-map).
