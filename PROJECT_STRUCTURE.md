# @Slaydtopbot - Project Structure

## Overview

Bu Telegram bot foydalanuvchilardan hujjatlar buyurtma qilish, to'lov qilish va hujjatlarni olish imkonini beradi.

## Fayl Tuzilishi

```
telegram-bot/
├── bot.py                          # Asosiy bot kodlari
├── generate_documents.py           # Hujjat yaratish funksiyalari
├── requirements.txt                # Kutubxonalar ro'yxati
├── railway.json                    # Railway deployment konfiguratsiyasi
├── Procfile                        # Heroku deployment konfiguratsiyasi
├── runtime.txt                     # Python versiyasi
├── .gitignore                      # Git ignore fayli
├── README.md                       # Bot haqida ma'lumot
├── DEPLOYMENT_GUIDE.md             # Deployment qo'llanmasi
└── PROJECT_STRUCTURE.md            # Bu fayl
```

## Fayl Tafsilotlari

### 1. bot.py

**Vazifa**: Asosiy bot logikasi, to'lov tizimi va hujjat yaratish jarayonlari

**Asosiy funksiyalar**:
- `/start` - Botni boshlash
- `/help` - Yordam xabar
- `Yangi Taqdimot` - PowerPoint taqdimot yaratish
- `Fayl yoki URL bo'yicha taqdimot` - Fayl/URL asosida taqdimot
- `Slayd Pro (Rasm/Jadval/Chart)` - Kengaytirilgan taqdimot
- `Yangi Mustaqil ish` - Word hujjat (10 sahifa)
- `Yangi Referat` - Word referat
- `Tezis yaratish` - Word tezis
- `Maqola yaratish` - Word maqola

**To'lov tizimi**:
- Telegram Bot Payments API
- Payment provider tokeni orqali to'lov qabul qilish
- To'lov so'rovlari yuborish
- To'lov tasdiqlash

### 2. generate_documents.py

**Vazifa**: Hujjatlar yaratish funksiyalari

**Asosiy funksiyalar**:
- `generate_presentation()` - PowerPoint taqdimot yaratish
- `generate_word_document()` - Word hujjat yaratish
- `generate_report()` - Referat yaratish
- `generate_thesis()` - Tezis yaratish
- `generate_article()` - Maqola yaratish

**Kutubxonalar**:
- `python-pptx` - PowerPoint taqdimotlar uchun
- `python-docx` - Word hujjatlar uchun

### 3. requirements.txt

**Vazifa**: Bot uchun kerakli kutubxonalar ro'yxati

**Kutubxonalar**:
- `python-telegram-bot==21.9` - Telegram bot kutubxonasi
- `python-pptx==0.6.22` - PowerPoint yaratish
- `python-docx==1.1.2` - Word hujjatlar yaratish

### 4. railway.json

**Vazifa**: Railway platformasi uchun deployment konfiguratsiyasi

**Parametrlar**:
- `BOT_TOKEN` - Bot tokeni
- `PAYMENT_PROVIDER_TOKEN` - Payment provider tokeni

### 5. Procfile

**Vazifa**: Heroku platformasi uchun deployment konfiguratsiyasi

**Ishga tushirish buyrug'i**:
- `worker: python bot.py`

### 6. runtime.txt

**Vazifa**: Python versiyasini belgilash

**Versiya**: `python-3.11.0`

### 7. README.md

**Vazifa**: Bot haqida umumiy ma'lumot

**Mazmun**:
- Bot haqida
- Qanday foydalanish
- To'lov tizimi
- Hujjat yaratish

### 8. DEPLOYMENT_GUIDE.md

**Vazifa**: Botni Railway va Heroku'ga joylashtirish qo'llanmasi

**Mazmun**:
- Bot tokenini olish
- Payment provider tokenini olish
- Railway ga joylashtirish
- Heroku ga joylashtirish
- Xatolarni tuzatish

## Bot Ishlash Tartibi

### 1. Botni Boshlash

1. Foydalanuvchi botga `/start` buyrug'ini yuboradi
2. Bot menyusini ko'rsatadi
3. Foydalanuvchi hujjat turini tanlaydi

### 2. Ma'lumotlarni Yig'ish

1. Bot foydalanuvchidan quyidagilarni so'raydi:
   - Hujjat nomi
   - Mavzu
   - Ism va familiya
   - Sahifa soni (agar kerak bo'lsa)

### 3. To'lov Jarayoni

1. Bot to'lov so'rovi yuboradi
2. Foydalanuvchi to'lov amalga oshiradi
3. Bot to'lovni tasdiqlaydi
4. To'lov tasdiqlanganidan keyin hujjat yaratiladi

### 4. Hujjat Yaratish

1. Bot generate_documents.py faylidagi funksiyalarni chaqiradi
2. Hujjat yaratiladi
3. Bot hujjatni foydalanuvchiga yuboradi

## To'lov Tizimi

### To'lov Provayderlari

1. **YooKassa** - O'zbekiston va Rossiya uchun
2. **Stripe** - Xalqaro to'lovlar uchun
3. **Payme** - O'zbekiston uchun

### To'lov Miqdorlari

- **5-10 sahifa**: 5000 so'm
- **15-20 sahifa**: 10000 so'm
- **Har 5 sahifa**: +5000 so'm

## Hujjat Yaratish

### PowerPoint Taqdimotlar

- Sahifa soni: 5-25
- Format: .pptx
- Kutubxona: python-pptx

### Word Hujjatlar

- Format: .docx
- Kutubxona: python-docx
- Turlar:
  - Mustaqil ish (10 sahifa)
  - Referat
  - Tezis
  - Maqola

## Xavfsizlik

### Tokenlar

- **BOT_TOKEN**: Hech kimga bermang
- **PAYMENT_PROVIDER_TOKEN**: Hech kimga bermang
- **CARD_NUMBER**: Hech kimga bermang

### Environment Variables

- Railway/Heroku dashboardida saqlang
- Git repositoriyasiga yuklamang

## Xatolarni Tuzatish

### Bot ishlamayapti?

1. Loglarni tekshiring
2. Environment variables to'g'ri ekanligini tekshiring
3. Bot tokeni to'g'ri ekanligini tekshiring

### To'lov ishlamayapti?

1. Payment provider tokeni to'g'ri ekanligini tekshiring
2. Payment provider hisobingiz faol ekanligini tekshiring
3. Bot settingsida payments yoqilganligini tekshiring

### Hujjat yaratilmayapti?

1. generate_documents.py faylini tekshiring
2. Bot loglarini tekshiring
3. Kutubxonalar o'rnatilganligini tekshiring

## Qo'shimcha Xizmatlar

### Database

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

## Yordam

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

## Muhim Eslatmalar

1. **Tokenlarni saqlang**: Bot tokeni va payment tokeni maxfiy ma'lumotlar
2. **Bepul plan chegaralari**: Railway va Heroku bepul planlari cheklangan resurslarga ega
3. **To'lov provayderlari**: To'lov qabul qilish uchun faol payment provider hisobingiz kerak
4. **Hujjat yaratish**: Hujjat yaratish uchun python-pptx va python-docx kutubxonalari ishlatiladi

## Xulosa

Endi sizning @Slaydtopbot o'xshagan Telegram botingiz ishlayapti! Foydalanuvchilar bot orqali hujjatlar buyurtma qilishi, to'lov qilishi va hujjatlarini olishi mumkin.

Muvaffaqiyatli foydalanish!
