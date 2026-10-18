# Pembangunan

[English](Development) · [Dansk](Development-da) · **Bahasa Melayu**

## Semakan

```bash
python -m pytest        # ujian dengan liputan
ruff check .            # lint
ruff format --check .   # pemformatan
mypy src                # jenis, strict
doxygen Doxyfile        # dokumentasi sumber dalam docs/doxygen/
```

![Larian ujian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/raw/branch/main/docs/images/tests.png)

## Struktur

| Lapisan | Mengandungi |
| --- | --- |
| `domain` | Model, peraturan perubahan dan ralat; tiada rangkaian |
| `application` | Use case, format mesej dan port |
| `infrastructure` | HTTP, dua klien API, tetapan dan penghantar |
| `presentation` | Baris arahan |

Ujian hanya menggunakan fake: tiada ujian memanggil perkhidmatan sebenar atau membaca `.env` anda. Lihat [ADR-0001](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/src/branch/main/docs/adr/adr-0001-dependency-policy.md) untuk sebab HTTP menggunakan pustaka standard.
