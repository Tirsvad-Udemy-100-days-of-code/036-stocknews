# Udvikling

[English](Development) · **Dansk** · [Bahasa Melayu](Development-ms)

## Kontroller

```bash
python -m pytest        # tests med dækning
ruff check .            # lint
ruff format --check .   # formatering
mypy src                # typer, strict
doxygen Doxyfile        # kildedokumentation i docs/doxygen/
```

![Testkørsel](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/raw/branch/main/docs/images/tests.png)

## Opbygning

| Lag | Indeholder |
| --- | --- |
| `domain` | Modeller, ændringsreglen og fejl; intet netværk |
| `application` | Use casen, beskedformatet og portene |
| `infrastructure` | HTTP, de to API-klienter, indstillinger og afsenderen |
| `presentation` | Kommandolinjen |

Tests bruger kun fakes: ingen test kalder en rigtig tjeneste eller læser din `.env`. Se [ADR-0001](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/src/branch/main/docs/adr/adr-0001-dependency-policy.md) for hvorfor HTTP bruger standardbiblioteket.
