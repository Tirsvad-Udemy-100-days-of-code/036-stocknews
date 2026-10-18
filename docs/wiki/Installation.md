# Installation

**English** · [Dansk](Installation-da) · [Bahasa Melayu](Installation-ms)

## Requirements

Python 3.13 or newer, a free [Alpha Vantage key](https://www.alphavantage.co/support/#api-key) and a free [NewsAPI key](https://newsapi.org/register). The program has no runtime dependency; `pywhatkit` is only needed to send real messages.

## Steps

Create a local virtual environment, upgrade pip and install the project. On Windows activate it with `.venv\Scripts\Activate.ps1`, elsewhere with `source .venv/bin/activate`.

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

To send real messages install the optional extra: `python -m pip install -e ".[whatsapp]"`.

## Keys

Create a `.env` file in the project root. It is ignored by git; never commit it.

```text
APLHA_VANTAGE_API_KEY=your-alpha-vantage-key
NEWAPI_KEY=your-newsapi-key
PHONENUMBER=+4512345678
```
