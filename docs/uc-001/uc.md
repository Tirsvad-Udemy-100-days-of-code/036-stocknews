# Use Case: Receive Stock News Alert

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [UCD-001], [US-001], [SA-001], [SSD-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [9dd167b] |

---

## Format and Level

Format: Fully Dressed. Scope: Stock News program. Level: user-goal.

## Primary Actor

Investor (S01).

## Stakeholders and Interests

| Stakeholder | Interest |
| --- | --- |
| S01 | Learns at once why the stock moved |
| S02 | Can read and run the same flow |

## Preconditions

- The investor has a stock symbol, a company name and a threshold configured.
- The investor holds a price service key and a news service key.

## Postconditions (Success Guarantee)

- If the price moved by the threshold or more, the investor has received the news articles; otherwise nothing was sent.

## Main Success Scenario

1. The investor starts the program.
2. The system fetches the closing prices of the last two days.
3. The system calculates the percentage change.
4. The system finds that the change reaches the threshold.
5. The system fetches the latest news articles about the company.
6. The system sends one message per article to the investor.

## Extensions / Alternative Flows

- 2a. The price service answers with an error or a quota message: the system reports the reason and ends without sending.
- 4a. The change is below the threshold: the system reports that nothing happened and ends.
- 5a. The news service answers with an error: the system reports the reason and ends without sending.
- 6a. The investor started the program in dry-run mode: the system prints the messages instead of sending them.

## Special Requirements / Business Rules

| Step | Rule |
| --- | --- |
| 3 | Change = (yesterday's close - the day before's close) / the day before's close, in percent |
| 4 | The threshold is 5 percent, up or down, set in `constants.py` |
| 5 | Three articles, most recent first |
| 6 | Each message starts with the symbol, an up or down arrow and the percentage |

## Open Issues

None.

---

[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[SA-001]: ../stakeholder-analysis.md
[SSD-001]: ./ssd.md
[9dd167b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/commit/9dd167bdca930fedbf8e2ddd1beb9c2a552b2550
