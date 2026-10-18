# Installation

[English](Installation) · **Dansk** · [Bahasa Melayu](Installation-ms)

## Krav

Python 3.13 eller nyere, en gratis [Alpha Vantage-nøgle](https://www.alphavantage.co/support/#api-key) og en gratis [NewsAPI-nøgle](https://newsapi.org/register). Programmet har ingen runtime-afhængighed; `pywhatkit` skal kun bruges for at sende rigtige beskeder.

## Trin

Opret et lokalt virtuelt miljø, opgradér pip og installér projektet. På Windows aktiveres det med `.venv\Scripts\Activate.ps1`, ellers med `source .venv/bin/activate`.

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

For at sende rigtige beskeder installeres det valgfri tillæg: `python -m pip install -e ".[notify]"`.

## Nøgler

Opret en `.env`-fil i projektets rod. Git ignorerer den; læg den aldrig i et commit.

```text
APLHA_VANTAGE_API_KEY=your-alpha-vantage-key
NEWAPI_KEY=your-newsapi-key
STOCKNEWS_PHONE=+4512345678
```
