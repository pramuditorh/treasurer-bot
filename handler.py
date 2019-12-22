import telegram
import gsheet
import pandas as pd

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
		text="Treasurer Bot for Adaptive Network Laboratory Telkom University\n")

def kas(update, context):
    kas_gsheet = gsheet.getKas()
    df = pd.DataFrame(kas_gsheet)
    
    #for kas in kas_gsheet:
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text="Bayar Kas\n{}".format(df[['NAMA','AGUSTUS','SEPTEMBER'
                            ,'OKTOBER','NOVEMBER','DESEMBER','JANUARI','FEBRUARI','MARET','APRIL']]))