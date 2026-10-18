# Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [227594b] |

---

## Purpose

Decide whether the repository is ready to receive code: the project is configured, presentable and checked by CI.

## Deliverable

A repository with a description and topics, a Python `.gitignore`, `pyproject.toml`, an empty `src/stocknews` package with `constants.py`, a `Doxyfile`, CI workflows from `TirSystem/github-action`, a first README from the framework template, and an ADR for the dependency policy.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The repository has a description and at least five topics | Visible on the git host | Missing |
| 2 | `.env` and `config.env` are ignored by git | `git check-ignore` reports both | Either is tracked or not ignored |
| 3 | `pip install -e ".[dev]"` works in a fresh `.venv` on Python 3.13 | Exit code 0 | Fails |
| 4 | `framework/scripts/check-readme.sh` passes | Exit code 0 | Fails |
| 5 | The workflows are present and call `TirSystem/github-action` at `@v2` | Files present | Missing or invalid |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5, success criteria 3 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-19 — within the three-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set a clear description and topics (python, udemy, 100-days-of-code, stock-news, alpha-vantage, newsapi, pywhatkit) on the git host through its API, using the token in the local `.env`, so viewers (S03) can find the repository. | No | |
| 2 | Add Python .gitignore | Add a Python `.gitignore` that also ignores `.venv`, `.env`, `config.env` and Doxygen output, so secrets and build files are never committed. | No | |
| 3 | Add pyproject.toml and package skeleton | Configure the project for Python 3.13 or newer with an optional `notify` extra (`pywhatkit`) and a `dev` extra (pytest, pytest-cov, ruff, mypy), and create `src/stocknews` with `constants.py` and an empty `tests/` folder. | No | |
| 4 | Write ADR for the dependency policy | Record why HTTP uses the standard library and `pywhatkit` is an optional extra imported only when a message is sent, to satisfy S03 and the Business Case constraint. | No | |
| 5 | Add Doxyfile | Add a `Doxyfile` that documents `src/` from the Doxygen comments and writes to an ignored folder. | No | |
| 6 | Install CI workflows | Copy the quality, test, code-metrics, wiki and milestone workflows from `TirSystem/github-action` into `.gitea/workflows/`, pinned to `@v2`. | No | |
| 7 | Write README with venv guide | Write `README.md` from the framework template: how to create and use `.venv`, run `python -m pip install --upgrade pip`, install, run and test. | No | |

---

[BC-001]: ../business-case.md
[227594b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/commit/227594bb0fb1d03545a66ddb64df77c61fa92fa8
