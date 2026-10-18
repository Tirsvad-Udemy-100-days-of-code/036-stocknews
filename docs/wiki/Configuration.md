# Configuration

**English** · [Dansk](Configuration-da) · [Bahasa Melayu](Configuration-ms)

## Constants

Edit `src/stocknews/constants.py`.

| Constant | Meaning | Default |
| --- | --- | --- |
| `STOCK` | Stock symbol | `TSLA` |
| `COMPANY_NAME` | Name used to search the news | `Tesla Inc` |
| `THRESHOLD_PERCENT` | Change in percent that triggers an alert | `5.0` |
| `NEWS_COUNT` | Number of articles sent | `3` |

## Keys and phone number

| Variable | Meaning |
| --- | --- |
| `APLHA_VANTAGE_API_KEY` | Alpha Vantage key |
| `NEWAPI_KEY` | NewsAPI key |
| `STOCKNEWS_PHONE` | Your phone number with country code (not needed for `--dry-run`) |

Environment variables win over the files `.env` and `config.env` in the working directory. Both files are ignored by git.
