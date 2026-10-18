# Core features

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [227594b] |

---

## Purpose

Decide whether the program does what the assignment asks: alert on a 5 percent move with the latest news.

## Deliverable

The `stocknews` package in `src/`, tests in `tests/`, and a program that runs with `python -m stocknews`, including a dry-run mode.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes | Exit code 0 | Any failure |
| 2 | Coverage of `src/` | At least 90 percent | Below 90 percent |
| 3 | `ruff check`, `ruff format --check` and `mypy --strict` pass | Exit code 0 | Any finding |
| 4 | No test calls a network service or imports the personal `.env` | Tests use fakes only | A real call exists |
| 5 | `python -m stocknews --dry-run` prints the alert without sending | Output shown | Crashes |
| 6 | The code is reviewed against `qc-programming-python` | A `Go` review record | A `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the project configuration and the plan gate |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 4, success criteria 1 to 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-21 — within the three-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Use case: receive a news alert | S01 runs the program and receives the latest news when the stock moved by the threshold; write UC-001 and its system sequence diagram. | Yes | UC-001 |
| 2 | Load settings | Read the two API keys, the recipient number and the dry-run flag from environment variables, with a small standard-library reader for a local `.env` that tests never import. | No | |
| 3 | Implement get_stock_prices | Call Alpha Vantage `TIME_SERIES_DAILY` with the standard library and return yesterday's and the day before's closing prices; report API errors and quota messages clearly. | No | |
| 4 | Implement calculate_change | Return the signed percentage change between two closes and decide whether its absolute value reaches the threshold in `constants.py`. | No | |
| 5 | Implement get_news | Call NewsAPI `everything` for the company name and return the first three articles with title and description. | No | |
| 6 | Implement message formatting and sending | Format the alert (symbol, arrow, percentage, headline, brief) and send it with `pywhatkit`, imported lazily; in dry-run mode print instead. | No | |
| 7 | Implement the program entry point | Wire the functions in `python -m stocknews` with `--dry-run`, exit codes and no secrets in output. | No | |
| 8 | Write unit tests | Cover every function with `pytest` using fake HTTP responses and a fake sender, and reach 90 percent coverage. | No | |

---

[BC-001]: ../business-case.md
[227594b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/commit/227594bb0fb1d03545a66ddb64df77c61fa92fa8
