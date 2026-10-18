# 🚀 Stock News (Day 36 of 100 Days of Code)

A small Python program that watches one stock and, when its closing price moved by 5 percent or more, sends you the latest news about the company. It is the Day 36 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", for coursists who want to compare solutions and for anyone browsing for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The program compares yesterday's closing price with the day before from [Alpha Vantage](https://www.alphavantage.co/), and, when the change reaches the threshold in `constants.py`, fetches the three latest articles from [NewsAPI](https://newsapi.org/) and sends them with `pywhatkit` (not Twilio).

| Folder | What it holds |
| --- | --- |
| `src/stocknews/` | The program, in the layers `domain`, `application`, `infrastructure` and `presentation`; `constants.py` holds the settings you may change |
| `tests/` | The `pytest` tests (`unit`, `integration`, `e2e`); they use fakes and never call a real service |
| `docs/` | Business case, plan, milestones, reviews and the wiki |
| `Doxyfile` | Configuration for the Doxygen documentation of the source |

## 📋 Requirements

- Python 3.13 or newer.
- A free Alpha Vantage API key ([get one](https://www.alphavantage.co/support/#api-key)) and a free NewsAPI key ([register](https://newsapi.org/register)).
- Only to send real messages: `pywhatkit` (optional extra `notify`), a desktop browser signed in to WhatsApp Web, and your phone number. Without it, use the dry run, which only prints.
- Optional: Doxygen, to build the source documentation.

The program itself has no runtime dependency.

## 🛠️ Setup

Create and use a local virtual environment, then upgrade pip and install the project.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

To send real messages also install the optional extra: `python -m pip install -e ".[notify]"`.

Put your keys in a local `.env` file in the project root. It is ignored by git and must never be committed:

```text
APLHA_VANTAGE_API_KEY=your-alpha-vantage-key
NEWAPI_KEY=your-newsapi-key
STOCKNEWS_PHONE=+4512345678
```

The variable name `APLHA_VANTAGE_API_KEY` is spelled as it is in the author's own file; it is defined once in `constants.py`.

## ▶️ Run

```bash
python -m stocknews --dry-run   # prints the alert, sends nothing
python -m stocknews             # sends the alert with pywhatkit
```

Change the stock, company name and threshold in `src/stocknews/constants.py`. Build the source documentation with `doxygen Doxyfile` (output in `docs/doxygen/`).

## 🧪 Tests

```bash
python -m pytest
ruff check .
mypy src
```

## 📄 License

[GNU Affero General Public License v3](./LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
