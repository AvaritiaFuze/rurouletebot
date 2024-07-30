from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
import secrets
import logging

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    token = secrets.token_urlsafe(16)
    save_token(user_id, token)
    
    keyboard = [
        [InlineKeyboardButton("Играть в Русскую рулетку", url=f"https://your-app-name.herokuapp.com?token={token}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать в игру Русская рулетка! Нажмите кнопку ниже, чтобы начать играть.", reply_markup=reply_markup)

def save_token(user_id, token):
    with open('tokens.txt', 'a') as f:
        f.write(f"{user_id},{token}\n")

def main():
    application = Application.builder().token("7015147664:AAG1UqUI3Z-zZBaq1iQTJ3T8coMWGSu4xpw").build()
    logger.info("Бот запущен")
    
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()