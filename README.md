# Gcore Product Documentation

Source of the Gcore documentation site at [docs.gcore.com](https://docs.gcore.com), built with [Mintlify](https://mintlify.com). Content is MDX, grouped by product (`cloud/`, `cdn/`, `dns/`, `waap/`, `streaming/`, `fastedge/`, and others). Site navigation is defined in `docs.json`.

## Preview locally

Install the Mintlify CLI once, then run it from the repo root (the folder that contains `docs.json`):

```
npm i -g mintlify
mintlify dev
```

If the preview does not start, run `mintlify install` to reinstall dependencies. If a page returns 404, check that you are in the folder with `docs.json`.

On Windows, run `git config --global core.longpaths true` once after cloning, because some image paths exceed the default path length limit.

## Writing and editing articles

- [CONTRIBUTING.md](CONTRIBUTING.md) - guide for writers: the tabbed `MethodSwitch` article pattern, frontmatter, links, and debugging MDX build errors.
- [.agents/references/style-guide.md](.agents/references/style-guide.md) - voice, structure, and formatting rules.

## Working with AI agents

[AGENTS.md](AGENTS.md) holds the repo-wide rules for AI agents and a table that maps each task to a skill in `.claude/skills/`. Claude Code reads it through `CLAUDE.md`.

## Automation

GitHub Actions in `.github/workflows/` normalize images, sanitize frontmatter, regenerate `llms.txt`, validate Terraform examples, and track API, SDK, and Terraform provider changes. The full list and what each one does to a pull request is in [AGENTS.md](AGENTS.md). Do not push directly to `main`; open a pull request.
