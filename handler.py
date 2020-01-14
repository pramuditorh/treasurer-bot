import telegram
import gsheet
import pandas as pd
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
		text="Treasurer Bot for Adaptive Network Laboratory Telkom University\n")

def kas(update, context):
    kas_gsheet = gsheet.getKas()
    text = update.message.text.split()
    #nama = text[1].capitalize()
    bulan = text[1].upper()
    df = pd.DataFrame(kas_gsheet)
    df.index += 1

    print(kas_gsheet)

    context.bot.send_message(chat_id=update.effective_chat.id,
                            text="Bayar Kas\n{}".format(df[['NAMA', bulan]]))