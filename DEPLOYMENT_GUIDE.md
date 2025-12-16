# Telegram Bot Deployment Guide

## Overview

Bu qo'llanma sizga @Slaydtopbot o'xshagan Telegram botni Railway platformasida bepul joylashtirishni o'rgatadi.

## Bot Xususiyatlari

- **To'lov tizimi**: Telegram Bot Payments API orqali to'lov qabul qiladi
- **Hujjat turlari**: 
  - PowerPoint taqdimotlar (5-25 sahifa)
  - Fayl/URL asosida taqdimotlar
  - Kengaytirilgan taqdimotlar (rasmlar, jadvallar, grafiklar)
  - Mustaqil ishlar (Word, 10 sahifa)
  - Referatlar (Word)
  - Tezislar (Word)
  - Maqolalar (Word)
- **Narxlar**: 5-10 sahifa - 5000 so'm, 15-20 sahifa - 10000 so'm, har 5 sahifa uchun +5000 so'm

## 1. Bot Tokenini oling

Agar sizda bot tokeni bo'lmasa, @BotFather orqali yangi bot yarating:

1. Telegramda @BotFather ga murojaat qiling
2. `/newbot` buyrug'ini yuboring
3. Bot nomini va foydalanuvchi nomini (username) kiriting
4. BotFather sizga token beradi (masalan: `7521874611:AAGbYynhe-NRmKUo2_AkjqTv2paRm6tZwOI`)

**Xavfsizlik ogohlantirishi**: Tokenni hech kimga bermang!

## 2. Payment Provider Token Oling

To'lov qabul qilish uchun sizga payment provider tokeni kerak. Telegram Bot Payments API uchun quyidagi provayderlardan birini tanlang:

### Variant 1: YooKassa (YoKassa)
1. [YooKassa saytiga](https://yookassa.ru/) kiring
2. Hisob yarating
3. Telegram bot uchun integration qo'shing
4. Payment token oling

### Variant 2: Stripe
1. [Stripe saytiga](https://stripe.com/) kiring
2. Hisob yarating
3. Telegram bot uchun integration qo'shing
4. Payment token oling

### Variant 3: Payme
1. [Payme saytiga](https://www.payme.uz/) kiring
2. Hisob yarating
3. Telegram bot uchun integration qo'shing
4. Payment token oling

## 3. Railway Platformasida Botni Joylashtirish

### 3.1. GitHub Repositoriyasi Yaratish

1. [GitHub.com](https://github.com/) ga kirib, yangi repositoriya yarating
2. Repositoriya nomi: `slaydtop-bot`
3. "Add .gitignore" -> "Python" ni tanlang
4. Repositoriyani yarating

### 3.2. Proyektni GitHub ga Yuklash

```bash
# Proyekt katalogiga o'ting
cd /home/ubuntu/telegram-bot

# Git repositoriyasi yarating
git init

# Barcha fayllarni qo'shing
git add .

# Commit qiling
git commit -m "Initial commit"

# GitHub repositoriyasiga bog'lang
git remote add origin https://github.com/YOUR_USERNAME/slaydtop-bot.git

# Push qiling
git push -u origin main
```

### 3.3. Railway Proyektini Yaratish

1. [Railway.app](https://railway.app/) ga kirib, "New Project" tugmasini bosing
2. "Deploy from GitHub" ni tanlang
3. GitHub repositoriyasini tanlang: `slaydtop-bot`
4. "Deploy" tugmasini bosing

### 3.4. Environment Variables Sozlash

Railway proyektini oching va "Variables" bo'limiga o'ting:

| Variable Name | Value |
|---------------|-------|
| BOT_TOKEN | Sizning bot tokeningiz |
| PAYMENT_PROVIDER_TOKEN | Payment provider tokeningiz |

### 3.5. Botni Ishga Tushiring

1. Railway dashboardida "Deploy" tugmasini bosing
2. Deployment jarayoni tugagach, bot avtomatik ishga tushadi
3. Botni Telegramda sinab ko'ring

## 4. Heroku Platformasida Botni Joylashtirish (Alternativa)

Agar Railway ishlatmoqchi bo'lmasangiz, Heroku ham ishlatishingiz mumkin:

### 4.1. Heroku Hisobini Yarating

1. [Heroku.com](https://heroku.com/) saytiga kiring
2. Hisob yarating
3. Bepul plan tanlang

### 4.2. Heroku CLI O'rnatish

```bash
# Mac
brew install heroku

# Windows
# Heroku CLI download: https://devcenter.heroku.com/articles/heroku-cli

# Linux
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```

### 4.3. Botni Heroku'ga Joylashtirish

```bash
# Heroku'ga login qiling
heroku login

# Yangi app yarating
heroku create your-bot-name

# Environment variables o'rnatish
heroku config:set BOT_TOKEN=your_bot_token
heroku config:set PAYMENT_PROVIDER_TOKEN=your_payment_token

# Deploy qilish
git init
git add .
git commit -m "Initial commit"
heroku git:remote -a your-bot-name
git push heroku main
```

## 5. Botni Telegramda Sinab Ko'rish

1. Telegramda botingizni oching
2. `/start` buyrug'ini yuboring
3. Menyu tugmalarini tekshiring
4. To'lov jarayonini sinab ko'ring
5. Hujjat yaratish funksiyasini tekshiring

## 6. Botni O'zgartirish va Yangilash

Botni o'zgartirish uchun:

1. `bot.py` faylini tahrirlang
2. `generate_documents.py` faylini tahrirlang (hujjat yaratish logikasi)
3. O'zgarishlarni saqlang
4. Railway/Heroku'ga yangi versiyani deploy qiling

## 7. Xatolarni Tuzatish

### Bot ishlamayapti?

1. Railway/Heroku dashboardida "Logs" bo'limini tekshiring
2. Environment variables to'g'ri kiritilganligini tekshiring
3. Bot tokeni va payment tokeni to'g'ri ekanligini tekshiring

### To'lov ishlamayapti?

1. Payment provider tokeni to'g'ri ekanligini tekshiring
2. Payment provider hisobingiz faol ekanligini tekshiring
3. Telegram bot settingsida payments yoqilganligini tekshiring

### Hujjat yaratilmayapti?

1. `generate_documents.py` faylini tekshiring
2. Bot loglarini tekshiring
3. Hujjat yaratish logikasini tekshiring

## 8. Qo'shimcha Xizmatlar

### Database (MongoDB/PostgreSQL)

Agar botingizga database kerak bo'lsa:

1. Railway dashboardida "Add" tugmasini bosing
2. "Database" ni tanlang
3. MongoDB yoki PostgreSQL tanlang
4. Database connection string oling
5. Bot kodiga qo'shing

### Monitoring

1. Railway dashboardida "Metrics" bo'limini tekshiring
2. Bot ishlashini kuzatib boring
3. Xatolarni tezda aniqlang

## 9. Yordam

### Telegram BotFather
- Bot sozlamalarini o'zgartirish
- Bot rasmini o'zgartirish
- Bot username'ini o'zgartirish

### Railway Support
- [Railway Docs](https://docs.railway.app/)
- [Railway Community](https://community.railway.app/)

### Heroku Support
- [Heroku Dev Center](https://devcenter.heroku.com/)
- [Heroku Forums](https://devcenter.heroku.com/)

## 10. Muhim Eslatmalar

1. **Tokenlarni saqlang**: Bot tokeni va payment tokeni maxfiy ma'lumotlar
2. **Bepul plan chegaralari**: Railway va Heroku bepul planlari cheklangan resurslarga ega
3. **To'lov provayderlari**: To'lov qabul qilish uchun faol payment provider hisobingiz kerak
4. **Hujjat yaratish**: Hujjat yaratish uchun `python-pptx` va `python-docx` kutubxonalari ishlatiladi

## Xulosa

Endi sizning @Slaydtopbot o'xshagan Telegram botingiz ishlayapti! Foydalanuvchilar bot orqali hujjatlar buyurtma qilishi, to'lov qilishi va hujjatlarini olishi mumkin.

Muvaffaqiyatli foydalanish!
