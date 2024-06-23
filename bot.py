from telegram.ext import ApplicationBuilder, MessageHandler

from config import TOKEN
from handlers import message_handler


bot = ApplicationBuilder().token(TOKEN).build()

bot.add_handler(message_handler)

if __name__ == '__main__':
    bot.run_polling()

