from telegram.ext import ApplicationBuilder, MessageHandler
import logging as bot_logger

bot_logger.basicConfig(
    level=bot_logger.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='bot_logs.log'
)

from config import TOKEN
from handlers import message_handler, reply_handler


bot = ApplicationBuilder().token(TOKEN).build()

bot.add_handler(message_handler)
bot.add_handler(reply_handler)

if __name__ == '__main__':
    try:
        bot_logger.info('start polling...')
        bot.run_polling()
    except (KeyboardInterrupt, SystemError, SyntaxError) as e:
        bot_logger.error(f'{type(e)}: {str(e)}')


