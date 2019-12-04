import logging
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from telegram.ext import Updater, CommandHandler
from credentials import TELEGRAM_TOKEN

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                    text="I'm a bot, please talk to me!")

def kas(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                    text="Kas")

start_handler = CommandHandler('start', start)
kas_handler = CommandHandler('kas', kas)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(kas_handler)
updater.start_polling()