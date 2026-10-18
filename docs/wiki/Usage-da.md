# Brug

[English](Usage) · **Dansk** · [Bahasa Melayu](Usage-ms)

## Kørsel

```bash
python -m stocknews --dry-run   # udskriver alarmen, sender intet
python -m stocknews             # sender alarmen med pywhatkit
```

## Sådan virker det

1. Hent de to seneste daglige lukkekurser fra Alpha Vantage.
2. Beregn ændringen i procent.
3. Er ændringen 5 procent eller mere, op eller ned, hentes tre artikler fra NewsAPI.
4. Send én besked pr. artikel: symbol, pil, procent, overskrift og resumé.

![Output fra dry run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/raw/branch/main/docs/images/dry-run.png)

`pywhatkit` åbner WhatsApp Web i din browser, så du skal være logget ind. Svarer en API med en fejl, eller er dagens kvote brugt, udskriver programmet årsagen og afslutter med kode 1.
