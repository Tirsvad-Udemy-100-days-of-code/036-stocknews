# Penggunaan

[English](Usage) · [Dansk](Usage-da) · **Bahasa Melayu**

## Jalankan

```bash
python -m stocknews --dry-run   # cetak amaran, tidak hantar apa-apa
python -m stocknews             # hantar amaran dengan pywhatkit
```

## Cara ia berfungsi

1. Ambil dua harga penutup harian terkini daripada Alpha Vantage.
2. Kira perubahan dalam peratus.
3. Jika perubahan 5 peratus atau lebih, naik atau turun, ambil tiga artikel daripada NewsAPI.
4. Hantar satu mesej bagi setiap artikel: simbol, anak panah, peratus, tajuk dan ringkasan.

![Output dry run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/036-stocknews/raw/branch/main/docs/images/dry-run.png)

`pywhatkit` membuka WhatsApp Web dalam pelayar anda, jadi anda mesti log masuk. Jika API membalas dengan ralat atau kuota harian telah habis, program mencetak sebabnya dan keluar dengan kod 1.
