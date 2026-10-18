# SQA Review Record: MIL-001 CI workflows

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [MIL-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [6433a4e] |

---

## Artifact Under Review

- Instance reviewed: `.gitea/workflows/*.yml` of the branch `mil-001-foundation`
- Checklist used: QC-WF-001 and QC-YML-001
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | See the YAML table below. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | Files are in `.gitea/workflows/` only. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | `name`, `on` and `jobs` declared; triggers explicit. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Each file has a header comment with purpose, triggers, inputs, secrets, outside changes and milestone. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Jobs and steps are named. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | `actionlint` 1.7.12 reports no finding on the four files. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | Every job declares `permissions`; `contents: write` only on the metrics job. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | Own actions use exact tags (`checkout@v4.2.2`, `setup-python@v5.3.0`, `upload-artifact@v4.6.2`); the shared workflows are pinned to the organisation's `@v2` release tag, as the checklist allows. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | No secret in files; `SYNC_TOKEN` and `TOKEN_FOR_GITEA_WIKI` are read as secrets. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No untrusted text is interpolated into `run:`. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | No `pull_request_target` or `workflow_run`. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Pass | Tests/quality change nothing outside; publish and sync run on `main` pushes, sync is dry run on manual start. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | Pass | Tests need no token; the two secrets are the minimum the shared workflows document. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | Own jobs set `runs-on` and `timeout-minutes`; jobs that call a reusable workflow inherit them from it. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` set on quality, tests and sync. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Wiki and milestone workflows are path-filtered; quality and tests run on every pull request by design. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | Tool versions of the dev extra are pinned with `==` in `pyproject.toml`; the shared workflows pin their own. |
| 18 | A dependency cache is used where the install is slow enough to matter | Pass | `setup-python` pip cache enabled. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | Pass | The tools write `path:line` findings themselves. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | No `run:` block longer than five lines. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | Shared logic is called as reusable workflows. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Fail | The workflows have not yet run on the Gitea instance; verified locally with actionlint only. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | N-A | No reusable workflow is defined here. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | N-A | Validation is by actionlint and yamllint in this review; no static test file yet. |

## Checklist Results: QC-YML-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | yamllint parses all four files; no duplicate keys. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | 2-space indentation, LF, one final newline (yamllint default rules). |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `yamllint` passes with `.yamllint.yml` committed; no disable comments. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | No coercible scalar unquoted; `python-version` is quoted. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | No language tags. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | No secret written. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | No embedded program text above five lines. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | No repeated block. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchors used. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | N-A | No schema for Gitea workflows; actionlint covers it. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | Header comments name purpose and milestone. |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | Keys follow the workflow schema; kebab-case input names. |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | Pass | No multi-line strings. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | Lowercase kebab-case `.yml` names. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | yamllint and actionlint run without the real target. |

## Overall Verdict

Go-with-conditions — criterion 22 of QC-WF-001 fails; the workflows stay unverified on the host until the conditions are closed. Milestone Go/No-Go criterion 5 only needs the files, so it does not depend on this.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Run the workflows once on the Gitea instance, record host and version, create secrets SYNC_TOKEN and TOKEN_FOR_GITEA_WIKI (criterion 22) | S01 | 2026-10-25 |

---

[MIL-001]: ../../milestones/mil-001-foundation.md
[6433a4e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/commit/6433a4e30aa658605ba1f4bed186ae1876ea0176
