# Konfiguration

[English](Configuration) · **Dansk** · [Bahasa Melayu](Configuration-ms)

## Konstanter

Ret `src/stocknews/constants.py`.

| Konstant | Betydning | Standard |
| --- | --- | --- |
| `STOCK` | Aktiesymbol | `TSLA` |
| `COMPANY_NAME` | Navn brugt til nyhedssøgning | `Tesla Inc` |
| `THRESHOLD_PERCENT` | Ændring i procent, der udløser en alarm | `5.0` |
| `NEWS_COUNT` | Antal artikler, der sendes | `3` |

## Nøgler og telefonnummer

| Variabel | Betydning |
| --- | --- |
| `APLHA_VANTAGE_API_KEY` | Alpha Vantage-nøgle |
| `NEWAPI_KEY` | NewsAPI-nøgle |
| `PHONENUMBER` | Dit telefonnummer med landekode (ikke nødvendigt med `--dry-run`) |

Miljøvariabler går forud for filerne `.env` og `config.env` i arbejdsmappen. Begge filer ignoreres af git.
