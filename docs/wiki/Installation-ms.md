# Pemasangan

[English](Installation) · [Dansk](Installation-da) · **Bahasa Melayu**

## Keperluan

Python 3.13 atau lebih baharu, [kunci Alpha Vantage](https://www.alphavantage.co/support/#api-key) percuma dan [kunci NewsAPI](https://newsapi.org/register) percuma. Program ini tiada kebergantungan runtime; `pywhatkit` hanya diperlukan untuk menghantar mesej sebenar.

## Langkah

Cipta persekitaran maya setempat, naik taraf pip dan pasang projek. Pada Windows aktifkan dengan `.venv\Scripts\Activate.ps1`, selain itu dengan `source .venv/bin/activate`.

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Untuk menghantar mesej sebenar, pasang tambahan pilihan: `python -m pip install -e ".[notify]"`.

## Kunci

Cipta fail `.env` dalam akar projek. Git mengabaikannya; jangan sekali-kali commit fail ini.

```text
APLHA_VANTAGE_API_KEY=your-alpha-vantage-key
NEWAPI_KEY=your-newsapi-key
STOCKNEWS_PHONE=+4512345678
```
