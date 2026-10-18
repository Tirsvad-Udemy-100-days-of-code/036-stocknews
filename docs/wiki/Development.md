# Development

**English** · [Dansk](Development-da) · [Bahasa Melayu](Development-ms)

## Checks

```bash
python -m pytest        # tests with coverage
ruff check .            # lint
ruff format --check .   # format
mypy src                # types, strict
doxygen Doxyfile        # source documentation in docs/doxygen/
```

![Test run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/raw/branch/main/docs/images/tests.png)

## Structure

| Layer | Holds |
| --- | --- |
| `domain` | Models, the change rule and errors; no network |
| `application` | The use case, the message format and the ports |
| `infrastructure` | HTTP, the two API clients, settings and the sender |
| `presentation` | The command line |

Tests use fakes only: no test calls a real service or reads your `.env`. See [ADR-0001](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/src/branch/main/docs/adr/adr-0001-dependency-policy.md) for why HTTP uses the standard library.
