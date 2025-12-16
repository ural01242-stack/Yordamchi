#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, LabeledPrice, InputInvoiceMessageContent
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters, ContextTypes, PreCheckoutQueryHandler

# Import document generation module
from generate_documents import generate_presentation, generate_word_document, generate_presentation_from_file

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Conversation states
SELECTING_TYPE, ENTERING_TOPIC, ENTERING_NAME, ENTERING_FILE_URL, SELECTING_PAGES = range(5)

# Bot token (replace with your actual token)
BOT_TOKEN = "7521874611:AAGbYynhe-NRmKUo2_AkjqTv2paRm6tZwOI"

# Payment provider token (replace with your actual token from @BotFather)
# You need to get this from @BotFather by using /mybots -> Bot Settings -> Payments
PAYMENT_PROVIDER_TOKEN = "YOUR_PAYMENT_PROVIDER_TOKEN_HERE"

# Your card number for receiving payments
CARD_NUMBER = "YOUR_CARD_NUMBER_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton("🚀 Yangi Taqdimot (Slayd)", callback_data='new_presentation')],
        [InlineKeyboardButton("📄 Fayl yoki URL bo'yicha taqdimot", callback_data='file_presentation')],
        [InlineKeyboardButton("🚀 Slayd Pro (Rasm/Jadval/Chart)", callback_data='pro_presentation')],
        [InlineKeyboardButton("📄 Yangi Mustaqil ish", callback_data='independent_work')],
        [InlineKeyboardButton("📚 Yangi Referat", callback_data='reference')],
        [InlineKeyboardButton("📌 Tezis yaratish", callback_data='thesis')],
        [InlineKeyboardButton("✅ Maqola yaratish", callback_data='article')],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f'Assalomu alaykum, {user.first_name}! \n\n'
        'Slaydtop botga xush kelibsiz! \n\n'
        'Quyidagi tugmalardan birini tanlang:',
        reply_markup=reply_markup
    )
    
    return SELECTING_TYPE

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks"""
    query = update.callback_query
    await query.answer()
    
    document_type = query.data
    context.user_data['document_type'] = document_type
    
    # Get document type name
    doc_names = {
        'new_presentation': 'Yangi Taqdimot (Slayd)',
        'file_presentation': 'Fayl yoki URL bo\'yicha taqdimot',
        'pro_presentation': 'Slayd Pro (Rasm/Jadval/Chart)',
        'independent_work': 'Mustaqil ish',
        'reference': 'Referat',
        'thesis': 'Tezis',
        'article': 'Maqola'
    }
    
    doc_name = doc_names.get(document_type, 'hujjat')
    
    await query.edit_message_text(
        text=f'Siz "{doc_name}" yaratishni tanladingiz. \n\n'
             'Endi quyidagi ma\'lumotlarni kiriting:',
        reply_markup=ReplyKeyboardRemove()
    )
    
    # Ask for topic
    await query.message.reply_text(
        'Hujjat mavzusini kiriting:'
    )
    
    return ENTERING_TOPIC

async def enter_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle topic input"""
    topic = update.message.text
    context.user_data['topic'] = topic
    
    await update.message.reply_text(
        'Ism va familiyangizni kiriting:'
    )
    
    return ENTERING_NAME

async def enter_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle name input"""
    full_name = update.message.text
    context.user_data['full_name'] = full_name
    
    document_type = context.user_data['document_type']
    
    # If file-based presentation, ask for file/URL
    if document_type == 'file_presentation':
        await update.message.reply_text(
            'Fayl yoki URL manzilini yuboring:'
        )
        return ENTERING_FILE_URL
    
    # Otherwise, ask for number of pages
    return await ask_pages(update, context)

async def enter_file_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle file or URL input"""
    file_content = update.message.text
    context.user_data['file_url'] = file_content
    
    return await ask_pages(update, context)

async def ask_pages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ask for number of pages"""
    document_type = context.user_data['document_type']
    
    # Show page options
    keyboard = [
        [InlineKeyboardButton("5-10 sahifa (5000 so'm)", callback_data='5-10')],
        [InlineKeyboardButton("15-20 sahifa (10000 so'm)", callback_data='15-20')],
        [InlineKeyboardButton("25-30 sahifa (15000 so'm)", callback_data='25-30')],
        [InlineKeyboardButton("35-40 sahifa (20000 so'm)", callback_data='35-40')],
        [InlineKeyboardButton("45-50 sahifa (25000 so'm)", callback_data='45-50')],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        'Hujjat necha sahifadan iborat bo\'lishini tanlang:',
        reply_markup=reply_markup
    )
    
    return SELECTING_PAGES

async def select_pages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle page selection and send invoice"""
    query = update.callback_query
    await query.answer()
    
    pages = query.data
    context.user_data['pages'] = pages
    
    # Calculate price based on pages
    price_map = {
        '5-10': 5000,
        '15-20': 10000,
        '25-30': 15000,
        '35-40': 20000,
        '45-50': 25000
    }
    
    price = price_map.get(pages, 5000)
    
    # Get document type name
    doc_names = {
        'new_presentation': 'Yangi Taqdimot (Slayd)',
        'file_presentation': 'Fayl yoki URL bo\'yicha taqdimot',
        'pro_presentation': 'Slayd Pro (Rasm/Jadval/Chart)',
        'independent_work': 'Mustaqil ish',
        'reference': 'Referat',
        'thesis': 'Tezis',
        'article': 'Maqola'
    }
    
    doc_name = doc_names.get(context.user_data['document_type'], 'Hujjat')
    
    # Send invoice
    await query.edit_message_text(
        text=f'Siz tanlagan variant: {doc_name} ({pages} sahifa) \n\n'
             f'Narxi: {price} so\'m \n\n'
             'To\'lovni amalga oshirish uchun quyidagi tugmani bosing:',
        reply_markup=ReplyKeyboardRemove()
    )
    
    await query.message.reply_invoice(
        title=f'{doc_name} ({pages} sahifa)',
        description=f'Hujjat mavzusi: {context.user_data["topic"]}',
        payload=f'document_{context.user_data["document_type"]}_{pages}',
        provider_token=PAYMENT_PROVIDER_TOKEN,
        currency="UZS",
        prices=[LabeledPrice(f"{doc_name} ({pages} sahifa)", price * 100)],  # Price in cents
        start_parameter='document_payment'
    )
    
    return ConversationHandler.END

async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle pre-checkout query"""
    query = update.pre_checkout_query
    
    # Check the payload
    if not query.invoice_payload.startswith('document_'):
        await query.answer(ok=False, error_message="Xato to'lov ma'lumotlari")
        return
    
    await query.answer(ok=True)

async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle successful payment"""
    # Save payment information
    payment_info = {
        'user_id': update.effective_user.id,
        'user_name': update.effective_user.full_name,
        'document_type': context.user_data.get('document_type'),
        'topic': context.user_data.get('topic'),
        'full_name': context.user_data.get('full_name'),
        'pages': context.user_data.get('pages'),
        'file_url': context.user_data.get('file_url'),
        'payment_date': update.message.date.isoformat(),
        'amount': update.message.successful_payment.total_amount / 100,  # Convert cents to UZS
        'currency': update.message.successful_payment.currency
    }
    
    # Save payment data
    await save_payment_data(payment_info)
    
    # Generate document
    await generate_document(update, context, payment_info)
    
    # Send confirmation
    await update.message.reply_text(
        '✅ To\'lov muvaffaqiyatli amalga oshirildi! \n\n'
        'Hujjat yaratilmoqda, biroz kuting...'
    )

async def save_payment_data(payment_info):
    """Save payment information to file"""
    import json
    from datetime import datetime
    
    filename = f"/home/ubuntu/telegram-bot/payment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(payment_info, f, ensure_ascii=False, indent=2)
    
    logger.info(f"Saved payment data to {filename}")

async def generate_document(update: Update, context: ContextTypes.DEFAULT_TYPE, payment_info):
    """Generate document based on payment information"""
    import time
    
    document_type = payment_info['document_type']
    
    # Generate appropriate document
    if document_type in ['new_presentation', 'pro_presentation']:
        # Generate PowerPoint presentation
        await generate_presentation_document(update, payment_info)
    elif document_type == 'file_presentation':
        # Generate presentation from file/URL
        await generate_presentation_from_file_document(update, payment_info)
    else:
        # Generate Word document
        await generate_word_document_document(update, payment_info)

async def generate_presentation_document(update: Update, payment_info):
    """Generate PowerPoint presentation"""
    import os
    
    # Generate presentation
    output_path = f'/home/ubuntu/telegram-bot/{payment_info["user_id"]}_presentation.pptx'
    
    generate_presentation(
        title=payment_info['topic'],
        pages=payment_info['pages'],
        output_path=output_path
    )
    
    # Send document
    await update.message.reply_document(
        document=open(output_path, 'rb'),
        caption=f'✅ Sizning PowerPoint taqdimotingiz tayyor! \n\n'
                f'Hujjat turi: Yangi Taqdimot \n'
                f'Mavzu: {payment_info["topic"]} \n'
                f'Sahifalar soni: {payment_info["pages"]} \n\n'
                'Muvaffaqiyatli to\'lov uchun rahmat!'
    )

async def generate_presentation_from_file_document(update: Update, payment_info):
    """Generate presentation from file or URL"""
    import os
    
    # Generate presentation
    output_path = f'/home/ubuntu/telegram-bot/{payment_info["user_id"]}_presentation_from_file.pptx'
    
    generate_presentation_from_file(
        title=payment_info['topic'],
        file_url=payment_info.get('file_url', 'N/A'),
        pages=payment_info['pages'],
        output_path=output_path
    )
    
    # Send document
    await update.message.reply_document(
        document=open(output_path, 'rb'),
        caption=f'✅ Sizning taqdimotingiz tayyor! \n\n'
                f'Hujjat turi: Fayl/URL asosida taqdimot \n'
                f'Mavzu: {payment_info["topic"]} \n'
                f'Sahifalar soni: {payment_info["pages"]} \n\n'
                'Muvaffaqiyatli to\'lov uchun rahmat!'
    )

async def generate_word_document_document(update: Update, payment_info):
    """Generate Word document"""
    import os
    
    # Get document type name
    doc_names = {
        'independent_work': 'Mustaqil ish',
        'reference': 'Referat',
        'thesis': 'Tezis',
        'article': 'Maqola'
    }
    
    doc_name = doc_names.get(payment_info['document_type'], 'Hujjat')
    
    # Generate document
    output_path = f'/home/ubuntu/telegram-bot/{payment_info["user_id"]}_{payment_info["document_type"]}.docx'
    
    generate_word_document(
        title=payment_info['topic'],
        document_type=payment_info['document_type'],
        pages=payment_info['pages'],
        output_path=output_path
    )
    
    # Send document
    await update.message.reply_document(
        document=open(output_path, 'rb'),
        caption=f'✅ Sizning {doc_name.lower()}ingiz tayyor! \n\n'
                f'Hujjat turi: {doc_name} \n'
                f'Mavzu: {payment_info["topic"]} \n'
                f'Sahifalar soni: {payment_info["pages"]} \n\n'
                'Muvaffaqiyatli to\'lov uchun rahmat!'
    )

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancel the conversation."""
    await update.message.reply_text(
        'Jarayon bekor qilindi. Yangi hujjat yaratish uchun /start buyrug\'ini bering.',
        reply_markup=ReplyKeyboardRemove()
    )
    
    return ConversationHandler.END

def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Create conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECTING_TYPE: [CallbackQueryHandler(button_callback)],
            ENTERING_TOPIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, enter_topic)],
            ENTERING_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, enter_name)],
            ENTERING_FILE_URL: [MessageHandler(filters.TEXT & ~filters.COMMAND, enter_file_url)],
            SELECTING_PAGES: [CallbackQueryHandler(select_pages)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("cancel", cancel))
    application.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))
    
    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
