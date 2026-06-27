import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# === SOZLAMALAR ===
BOT_TOKEN = "8909999570:AAGj0lCf7DQLnztiEF9QkGQceeF3X7f6gtg"
OWNER_CHAT_ID = 8581449364  # Asadbek - xabar shu yerga keladi

logging.basicConfig(level=logging.INFO)

# === /start buyrug'i ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("✅ Boraman!", callback_data="boraman"),
            InlineKeyboardButton("❌ Kela olmayman", callback_data="kelolmayman"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎉 *Tug'ilgan kun taklifnomasi!*\n\n"
        "🎂 *Asadbek & Dilrabo*ning tug'ilgan kuniga taklif etilasiz!\n\n"
        "📅 *Sana:* 1-Iyul 2026, Chorshanba\n"
        "🕖 *Vaqt:* Kechki 19:00 – 20:00\n\n"
        "Kelasizmi? 👇",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# === Tugma bosilganda ===
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user
    ism = f"{user.first_name or ''} {user.last_name or ''}".strip()
    username = f"@{user.username}" if user.username else "username yo'q"

    if query.data == "boraman":
        # Foydalanuvchiga javob
        await query.edit_message_text(
            "🎊 Zo'r! Sizni kutamiz!\n\n"
            "📅 1-Iyul, Kechki 19:00 da ko'rishguncha! 🎂"
        )
        # Egasiga xabar
        await context.bot.send_message(
            chat_id=OWNER_CHAT_ID,
            text=f"✅ *Boraman* dedi!\n\n"
                 f"👤 Ism: {ism}\n"
                 f"🔗 Username: {username}\n"
                 f"🆔 ID: `{user.id}`",
            parse_mode="Markdown"
        )

    elif query.data == "kelolmayman":
        # Foydalanuvchiga javob
        await query.edit_message_text(
            "😢 Tushunarli, keyingi safar albatta!\n"
            "Baribir tabriklaymiz! 🎂"
        )
        # Egasiga xabar
        await context.bot.send_message(
            chat_id=OWNER_CHAT_ID,
            text=f"❌ *Kela olmayman* dedi.\n\n"
                 f"👤 Ism: {ism}\n"
                 f"🔗 Username: {username}\n"
                 f"🆔 ID: `{user.id}`",
            parse_mode="Markdown"
        )

# === Botni ishga tushirish ===
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("✅ Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
