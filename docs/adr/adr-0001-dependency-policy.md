# Dependency policy: standard library HTTP, optional pywhatkit

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [MIL-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [9761db7] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The program calls two HTTP APIs (Alpha Vantage and NewsAPI) and sends a message with `pywhatkit`. The Business Case limits runtime dependencies to those that are needed, and GitHub viewers (S03) want nothing to install just to read the code. Options for HTTP: (1) `requests`, the library the course uses; (2) `urllib.request` from the standard library. Options for sending: (1) a hard dependency on `pywhatkit`; (2) an optional extra imported only when a message is sent. `pywhatkit` opens a browser and pulls in several packages, so it is costly to install and impossible to test on a server.

## Decision

HTTP uses `urllib.request` from the standard library, and `pywhatkit` is declared as the optional extra `notify`, imported inside the sender function only when a real message is sent.

## Consequences

**Positive:**

- The default installation has no runtime dependency.
- Tests and the dry run need nothing but the standard library.
- The sender is isolated behind a port, so it can be replaced.

**Negative:**

- `urllib.request` is less convenient than `requests`; the small HTTP helper is ours to maintain.
- A user who wants real messages must install `.[notify]`.

## Affected Artifacts

- [BC-001] — meets the constraint "runtime dependencies only where needed"
- [MIL-001] — the package configuration follows this decision

---

[BC-001]: ../business-case.md
[MIL-001]: ../milestones/mil-001-foundation.md
[9761db7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/commit/9761db70f569899eecfe65a298a13184362ff19e
