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

    kas_handler = CommandHandler('kas', handler.kas)
    dp.add_handler(kas_handler)

    #tes_handler = CommandHandler('tes', handler.tes)
    #dp.add_handler(tes_handler)
    
    updater.start_polling()

if __name__ == '__main__':
	main()