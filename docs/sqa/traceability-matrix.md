# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [ADR-0001], [UCD-001], [US-001], [UC-001], [SSD-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | S01 | Added ADR-0001 | [9761db7] |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | S01 | Added UCD-001, US-001, UC-001, SSD-001 | pending |

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
| [UCD-001] | UCD | en | it | [SA-001], [BC-001] | [US-001], [UC-001] | RC-009 |
| [US-001] | US | en | it | [UCD-001], [BC-001] | [UC-001] | RC-010 |
| [UC-001] | UC | en | it | [UCD-001], [US-001], [MIL-002] | [SSD-001] | RC-011 |
| [SSD-001] | SSD | en | it | [UC-001] | - | RC-012 |
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
[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[UC-001]: ../uc-001/uc.md
[SSD-001]: ../uc-001/ssd.md
[9761db7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/commit/9761db70f569899eecfe65a298a13184362ff19e
