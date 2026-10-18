# SQA Review Record: MIL-002 source code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-002], [UC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: `src/` and `tests/` of the branch `mil-002-core-features`
- Checklist used: QC-PY-001
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | ruff `N` rules pass; modules snake_case, classes PascalCase, constants UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`calculate_change`, `PriceChange`, `ApiError`). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` clean; no `noqa`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` clean; every signature annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | Only specific exceptions caught; each re-raised `from error` (`http.py`, `alpha_vantage.py`, `whatsapp.py`). |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin shadowed (ruff B and A-class rules, review). |
| 7 | Files, locks and connections are managed with context managers | Pass | `urlopen` and file reads use `with`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Docstrings with Doxygen tags on public items. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `logging` is used for diagnostics; `print` appears only for the product output of the dry run (`console.py`) and stderr error text (`cli.py`); keys and phone number are never logged (`Settings.__repr__` hides them, URL not in error text). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists. Deviation recorded here: for this small program the classes are thin adapters of the Protocols in `application/ports.py`, which are the design; no DCD is produced. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 55 tests named for behaviour; no network; the personal `.env` is never read (tests change to `tmp_path`). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` passes; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No runtime dependencies; `pywhatkit` optional extra imported lazily; dev tools pinned. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Constants once in `constants.py`; the message format once in `messages.py`. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Domain imports only the standard library; application imports domain; infrastructure imports domain; only `cli.py` names every layer. No cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One responsibility per module; the use case depends on Protocols and receives implementations. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers `domain`, `application`, `infrastructure`, `presentation`; tests `unit`, `integration`, `e2e`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names English, snake_case, no space. |

## Overall Verdict

Go — every Mandatory criterion passes; 55 tests, 100 percent branch coverage, ruff and mypy strict clean.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-10-18 |

---

[MIL-002]: ../../milestones/mil-002-core-features.md
[UC-001]: ../../uc-001/uc.md
