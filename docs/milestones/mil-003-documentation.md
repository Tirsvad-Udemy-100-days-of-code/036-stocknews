# Documentation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether coursists (S02) and viewers (S03) can understand, run and find the project.

## Deliverable

Screenshots, a final README with them, and a wiki with the same pages in English, Danish and Bahasa Malaysia.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `framework/scripts/check-languages.sh` and `check-readme.sh` pass | Exit code 0 | Any finding |
| 2 | Wiki page sets in `en`, `da` and `ms` are identical | Same page list per language | A page is missing |
| 3 | README and wiki contain at least two screenshots | Images present and render | Missing |
| 4 | Screenshots contain no secret or phone number | Reviewed | Any secret visible |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Screenshots show the running program |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5, success criteria 4 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-23 — within the three-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create screenshots | Capture the dry-run output and the test run with fake data into `docs/images/`, with no secret visible. | No | |
| 2 | Finalise README | Add the screenshots and the final run and test instructions to `README.md` and make `check-readme.sh` pass. | No | |
| 3 | Write the English wiki | Write the Home, Installation, Usage, Configuration and Development pages in `docs/wiki/` plus `_Sidebar.md`, with screenshots. | No | |
| 4 | Write the Danish wiki | Translate every English wiki page to `<Page>-da.md` with the language line. | No | |
| 5 | Write the Bahasa Malaysia wiki | Translate every English wiki page to `<Page>-ms.md` with the language line. | No | |
| 6 | Check the wiki languages | Run `check-languages.sh` and fix gaps so the page sets match. | No | |

---

[BC-001]: ../business-case.md
