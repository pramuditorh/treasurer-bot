import logging
import config
import gsheet
import handler
from telegram.ext import Updater, CommandHandler

def main():
    updater = Updater(token=config.TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    start_handler = CommandHandler('start', handler.start)
    dp.add_handler(start_handler)
    
    updater.start_polling()

if __name__ == '__main__':
	main()