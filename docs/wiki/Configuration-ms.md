# Konfigurasi

[English](Configuration) · [Dansk](Configuration-da) · **Bahasa Melayu**

## Pemalar

Ubah `src/stocknews/constants.py`.

| Pemalar | Maksud | Lalai |
| --- | --- | --- |
| `STOCK` | Simbol saham | `TSLA` |
| `COMPANY_NAME` | Nama untuk mencari berita | `Tesla Inc` |
| `THRESHOLD_PERCENT` | Perubahan dalam peratus yang mencetuskan amaran | `5.0` |
| `NEWS_COUNT` | Bilangan artikel yang dihantar | `3` |

## Kunci dan nombor telefon

| Pemboleh ubah | Maksud |
| --- | --- |
| `APLHA_VANTAGE_API_KEY` | Kunci Alpha Vantage |
| `NEWAPI_KEY` | Kunci NewsAPI |
| `PHONENUMBER` | Nombor telefon anda dengan kod negara (tidak perlu untuk `--dry-run`) |

Pemboleh ubah persekitaran mengatasi fail `.env` dan `config.env` dalam direktori kerja. Kedua-dua fail diabaikan oleh git.
