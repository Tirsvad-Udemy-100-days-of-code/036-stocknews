# Usage

**English** · [Dansk](Usage-da) · [Bahasa Melayu](Usage-ms)

## Run

```bash
python -m stocknews --dry-run   # prints the alert, sends nothing
python -m stocknews             # sends the alert with pywhatkit
```

## How it works

1. Fetch the last two daily closing prices from Alpha Vantage.
2. Calculate the change in percent.
3. If the change is 5 percent or more, up or down, fetch three articles from NewsAPI.
4. Send one message per article: symbol, arrow, percentage, headline and brief.

![Dry run output](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/raw/branch/main/docs/images/dry-run.png)

`pywhatkit` opens WhatsApp Web in your browser, so you must be signed in. If an API answers with an error or its daily quota is used, the program prints the reason and exits with code 1.
