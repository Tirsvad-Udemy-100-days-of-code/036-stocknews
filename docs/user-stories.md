# User Stories

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [UCD-001], [BC-001], [MIL-002], [UC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose and Scope

The stories of gateway [MIL-002]: the investor receives an alert with news when the watched stock moves.

## Story List

### US-001.01

**As a** Investor, **I want** to receive the latest news about my stock when its closing price moved by the threshold, **so that** I can see why the price moved.

**Acceptance Criteria**

- Given the last two closing prices differ by 5 percent or more, when I run the program, then I receive the stock symbol, the direction, the percentage and three news articles.
- Given the prices differ by less than the threshold, when I run the program, then no message is sent.
- Given I run the program with the dry-run option, when the prices differ by the threshold, then the alert is printed and nothing is sent.

**Traces to:** [UC-001], [MIL-002]

**Size:** fits one iteration.

## INVEST Check

Independent, Negotiable, Valuable, Estimable, Small and Testable: yes, no exception.

---

[UCD-001]: ./use-case-diagram.md
[BC-001]: ./business-case.md
[MIL-002]: ./milestones/mil-002-core-features.md
[UC-001]: ./uc-001/uc.md
