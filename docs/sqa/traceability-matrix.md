# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [227594b] |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | S01 | Added ADR-0001 | [9761db7] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003] | RC-001 |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | RC-002 |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | - |
| [MIL-001] | MIL | en | it | [BC-001] | [MIL-002] | RC-003 |
| [MIL-002] | MIL | en | it | [BC-001], [MIL-001] | [MIL-003] | RC-004 |
| [MIL-003] | MIL | en | it | [BC-001], [MIL-002] | - | RC-005 |
| [ADR-0001] | ADR | - | - | [BC-001], [MIL-001] | - | RC-006 |

## Coverage Notes

The Project Plan has no QC checklist yet; S01 accepts it. No use case, design, code or ADR instance exists yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-core-features.md
[MIL-003]: ../milestones/mil-003-documentation.md
[ADR-0001]: ../adr/adr-0001-dependency-policy.md
[227594b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/commit/227594bb0fb1d03545a66ddb64df77c61fa92fa8
[9761db7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/commit/9761db70f569899eecfe65a298a13184362ff19e
