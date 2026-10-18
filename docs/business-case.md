# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [227594b] |

---

## Executive Summary

Stock prices move on news, and a private investor rarely sees the news in time. This project is the Day 36 assignment of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp": a small Python program that compares the last two closing prices of one stock and, when the price moved by 5 percent or more, fetches the latest news about the company and sends it as a message. The course participant (S01) builds it, Udemy coursists (S02) can read and run it, and GitHub viewers (S03) can browse it for ideas.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/`: a plan-first workflow in which each artifact is reviewed against its QC checklist before the next step. Quality is described with ISO/IEC 25010:2023 characteristics. Source code follows the `coding-conventions` skill (Python) and the layering of the `clean-architecture` skill, scaled to a small program.

## Problem Statement

- A price move of several percent is visible, but the reason for it is not, unless the investor searches the news by hand.
- Professional terminals give price and news together, but are too costly for a private learner.
- The assignment has to be solved as a complete, runnable program, not as loose snippets.

## Business Opportunity

Two free APIs (Alpha Vantage for prices, NewsAPI for articles) and one small notification library give a personal "mini terminal". Building it practises API reading, JSON handling, percentage calculation and messaging, and leaves a public example for other coursists.

## Objectives

1. Fetch the daily closing prices of one configured stock from Alpha Vantage and compare yesterday's close with the day before.
2. Detect a change of at least the configured threshold (5 percent, set in `constants.py`), up or down.
3. Fetch the three latest news articles about the configured company from NewsAPI when the threshold is crossed.
4. Send one message per article through `pywhatkit`, headed by the stock symbol, the direction and the percentage.
5. Deliver the repository as readable, tested, documented code with a Doxygen configuration, a README and a wiki in English, Danish and Bahasa Malaysia.

## Scope

### In Scope

- One stock, configured in `src/stocknews/constants.py` (default `TSLA`, "Tesla Inc").
- Price retrieval, change calculation, news retrieval, message formatting and message sending.
- API keys and the phone number read from environment variables or a local `.env` file that is never committed.
- Unit tests with `pytest`; no test calls a real API or sends a real message.
- `pyproject.toml`, `.gitignore`, a local `.venv` guide, `Doxyfile`, a README from the framework template, screenshots and a three-language wiki.
- Repository description and topics, and the CI workflows from `TirSystem/github-action`.

### Out of Scope

- Several stocks, scheduling, a database, a user interface or deployment.
- Twilio (replaced by `pywhatkit` for this project).
- Trading, investment advice or any financial transaction.
- Importing or testing the author's personal `.env` / `config.env` files; they are for the author's own use only.

## Expected Benefits

### Tangible Benefits

- A runnable program that solves the assignment.
- A public repository other coursists can read and run.

### Intangible Benefits

- Practice in reading API documentation, planning before coding and writing tests.
- A worked example of the framework workflow on a small project.

## Strategic Alignment

The project supports the author's learning goal in the bootcamp (Day 36) and the framework's goal of showing that a plan-first, reviewed workflow also fits a small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Tests pass | All `pytest` tests green on Python 3.13 | `python -m pytest` exits with 0 |
| 2 | Logic is covered by tests | At least 90 percent of lines in `src/` | `pytest --cov` report |
| 3 | Runtime dependencies | At most one (`pywhatkit`), as an optional extra | `pyproject.toml` |
| 4 | Wiki languages | Identical page sets in en, da and ms | `framework/scripts/check-languages.sh` and review |
| 5 | Repository presentation | Description, topics and a README with screenshots | Visible on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The free API quota is small (Alpha Vantage allows 25 requests a day) | A run fails with a quota message | The code reports the API error clearly; tests use fake responses |
| A secret is committed | Key exposure | `.gitignore` covers `.env` and `config.env`; secrets are never printed or tested |
| `pywhatkit` needs a desktop browser signed in to WhatsApp Web | Sending fails on a server | The sender is isolated behind one function and is an optional extra; a dry-run mode prints instead of sending |
| Screenshots show private data | Privacy leak | Screenshots use fake data and a dry run |

## Assumptions

- S01 holds free API keys for both services.
- The recipient number is the author's own, supplied by an environment variable.
- Python 3.13 or newer is installed.
- Coursists and viewers can reach the repository over the web.

## Constraints

- Python 3.13 or newer, `venv`, `pytest`, `pyproject.toml`, `constants.py`.
- Folder structure `src/`, `tests/`, `docs/`.
- Doxygen comments in source, with a `Doxyfile`.
- Runtime dependencies only where needed.
- Work proceeds on branches and pull requests, one per milestone.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About three days of the author's spare time; free API tiers; no hosting | A completed assignment, a public example and a reusable workflow (qualitative, because this is a learning project) |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment and owns scope, code and review |
| S02 | Reads and runs the code and compares solutions |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, the APIs are free and the result is useful to the author and to other coursists.

---

[SA-001]: ./stakeholder-analysis.md
[227594b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/commit/227594bb0fb1d03545a66ddb64df77c61fa92fa8
