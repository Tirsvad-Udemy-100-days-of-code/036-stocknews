# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

This analysis names the people who use or judge the project, so that owners, reviewers and recipients in every other document cite a stable ID. It uses the Power/Interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the assignment with clean, working and reviewed work |
| S02 | Udemy coursists | Fellow learners who share and compare solutions | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code that uses the assignment's function names, with instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear description, topics and README, and no runtime dependencies to install |

## Power/Interest Classification Rationale

- **Manage Closely:** S01 decides scope and accepts every artifact.
- **Keep Informed:** S02 cannot change the project but depends on its clarity.
- **Monitor:** S03 has neither influence nor a stake; a good first impression is enough.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Correct alert on a 5 percent move | Functionality |
| S01 | Tested, reviewed and documented work | Supportability |
| S02 | Easy to read and run | Usability |
| S02 | Function names follow the assignment | Functionality |
| S03 | No dependencies to install just to look | Implementation constraint |
| S03 | Findable through topics and description | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Pull request and run summary | All |
| S02 | README and wiki | At release | Run instructions, wiki in en, da and ms | MIL-003 |
| S03 | Repository page | At release | Description, topics, screenshots | MIL-001, MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 needs `pywhatkit` to send messages; S03 wants no runtime dependencies | S01, S03 | `pywhatkit` is an optional extra imported only when a message is sent; HTTP uses the standard library |
| S02 wants the assignment's function names; Clean Architecture asks for layers | S02, S01 | A small layered package whose public functions carry the assignment's names |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct alert | [BC-001] objectives 1 to 4 |
| S02 | Readable, runnable code | [BC-001] objective 5 |
| S03 | Findable repository | [BC-001] objective 5 |

## Sign-Off

S01, 2026-10-18; accepted through RC-002.

---

[BC-001]: ./business-case.md
