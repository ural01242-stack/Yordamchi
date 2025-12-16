# Slaydtop Bot - Telegram Bot Project

## Tavsif
Bu Telegram bot @Slaydtopbot kabi ishlaydi va foydalanuvchilardan hujjat turi, mavzu, ism-familiya va boshqa ma'lumotlarni olib, turli xil hujjatlarni (taqdimotlar, mustaqil ishlar, referatlar, tezislar, maqolalar) yaratishga yordam beradi. Bot to'lov tizimi orqali foydalanuvchilardan to'lov olib, pulni sizning karta raqamingizga o'tkazadi.

## O'rnatish

### 1. Bot tokenini o'zgartiring

Botni ishga tushirishdan oldin, `bot.py` faylida quyidagi qatorni o'zgartiring:

```python
BOT_TOKEN = "7521874611:AAGbYynhe-NRmKUo2_AkjqTv2paRm6tZwOI"
```

O'rniga o'z bot tokeningizni kiriting.

### 2. To'lov provider tokenini o'zgartiring

Telegram Bot Payments API uchun to'lov provider tokeni kerak. @BotFather orqali token olish uchun:

1. @BotFather ga kirib, `/mybots` buyrug'ini bering
2. Botni tanlang
3. "Bot Settings" -> "Payments" ni tanlang
4. "Payment Provider" bo'limida to'lov provider tokenini oling (Stripe, YooKassa yoki boshqa)
5. `bot.py` faylida quyidagi qatorni o'zgartiring:

```python
PAYMENT_PROVIDER_TOKEN = "YOUR_PAYMENT_PROVIDER_TOKEN_HERE"
```

### 3. Karta raqamini o'zgartiring

To'lov sizning karta raqamingizga o'tkaziladi. `bot.py` faylida quyidagi qatorni o'zgartiring:

```python
CARD_NUMBER = "YOUR_CARD_NUMBER_HERE"
```

### 4. Kerakli kutubxonani o'rnatish

```bash
sudo pip3 install python-telegram-bot python-pptx python-docx
```

## Bot funksionalligi

Bot quyidagi tugmalarni ko'rsatadi:

1. **🚀 Yangi Taqdimot (Slayd)** - Yangi PowerPoint taqdimot yaratish
2. **📄 Fayl yoki URL bo'yicha taqdimot** - Mavjud fayl yoki URL asosida taqdimot yaratish
3. **🚀 Slayd Pro (Rasm/Jadval/Chart)** - Kengaytirilgan taqdimot (rasmlar, jadvallar, grafiklar bilan)
4. **📄 Yangi Mustaqil ish** - Mustaqil ish yaratish (Word)
5. **📚 Yangi Referat** - Referat yaratish (Word)
6. **📌 Tezis yaratish** - Tezis yaratish (Word)
7. **✅ Maqola yaratish** - Maqola yaratish (Word)

### To'lov tizimi

Bot quyidagi narxlar tizimini ishlatadi:

- **5-10 sahifa** - 5000 so'm
- **15-20 sahifa** - 10000 so'm
- **25-30 sahifa** - 15000 so'm
- **35-40 sahifa** - 20000 so'm
- **45-50 sahifa** - 25000 so'm

Har bir hujjat turi uchun foydalanuvchi sahifalar sonini tanlaydi va to'lov amalga oshirilgandan so'ng, bot hujjatni yaratib yuboradi.

## Botni ishga tushirish

```bash
python3 bot.py
```

Bot ishga tushgandan so'ng, Telegramda botingizni topib, `/start` buyrug'ini bering.

## Bot ishlash tartibi

1. Foydalanuvchi `/start` buyrug'ini beradi
2. Bot menyudagi tugmalarni ko'rsatadi
3. Foydalanuvchi hujjat turini tanlaydi
4. Bot mavzu va ism-familiya so'raydi
5. Agar "Fayl yoki URL bo'yicha taqdimot" tanlangan bo'lsa, bot fayl/URL so'raydi
6. Bot sahifalar sonini tanlash uchun variantlarni ko'rsatadi
7. Foydalanuvchi variantni tanlaydi
8. Bot to'lov invoice yuboradi
9. Foydalanuvchi to'lovni amalga oshiradi
10. Bot to'lovni qabul qiladi va hujjatni yaratadi
11. Bot yaratilgan hujjatni foydalanuvchiga yuboradi

## Foydalanuvchi ma'lumotlari

Barcha foydalanuvchi ma'lumotlari va to'lovlar `/home/ubuntu/telegram-bot/` katalogida JSON formatda saqlanadi:

- `user_data_*.json` - Foydalanuvchi ma'lumotlari
- `payment_*.json` - To'lov ma'lumotlari

## Hujjat yaratish

Bot quyidagi kutubxonalardan foydalanadi:

- **python-pptx** - PowerPoint taqdimotlar yaratish
- **python-docx** - Word hujjatlar yaratish

Hujjatlar quyidagi tuzilishga ega:

### PowerPoint taqdimotlar
- Sarlavha slaydi
- 3-11 ta kontent slaydi (sahifalar soniga qarab)
- Har bir slayd sarlavha va matn bilan

### Word hujjatlar
- Sarlavha
- Muallif ma'lumotlari
- 3-11 bo'lim (sahifalar soniga qarab)
- Xulosa
- Foydalanilgan adabiyotlar

## Serverga joylashtirish

Botni doimiy ishlashi uchun serverga joylashtirish kerak. Quyidagi bepul platformalardan foydalanish mumkin:

### 1. Railway.app

1. Railway.app ga kirib, hisob yarating
2. "New Project" tugmasini bosing
3. "Deploy from GitHub" ni tanlang
4. Proyektni GitHub ga yuklang
5. Railway proyektini GitHub repositoriyaga bog'lang
6. Railway avtomatik ravishda botni ishga tushiradi

### 2. Render.com

1. Render.com ga kirib, hisob yarating
2. "New" -> "Web Service" ni tanlang
3. GitHub repositoriyani bog'lang
4. Build command: `pip3 install python-telegram-bot python-pptx python-docx`
5. Start command: `python3 bot.py`
6. Deploy qiling

### 3. Heroku

1. Heroku ga kirib, hisob yarating
2. "New" -> "Create new app" ni tanlang
3. GitHub repositoriyani bog'lang
4. Procfile yarating: `worker: python3 bot.py`
5. Deploy qiling

### 4. PythonAnywhere

1. PythonAnywhere ga kirib, hisob yarating
2. "Web" -> "Add a new web app" ni tanlang
3. "Manual configuration" ni tanlang
4. Python versiyasini tanlang
5. WSGI fayl yarating va botni ishga tushiring

## Xavfsizlik ogohlantirishi

**DIQQAT!**

1. **Bot tokeningizni hech kimga bermang** - Agar token oshkor bo'lib qolsa, @BotFather orqali yangi token oling
2. **To'lov provider tokenini xavfsiz saqlang** - Bu token orqali to'lovlar amalga oshiriladi
3. **Karta raqamingizni xavfsiz saqlang** - To'lov sizning karta raqamingizga o'tkaziladi

## Muallif

Slaydtop Bot
