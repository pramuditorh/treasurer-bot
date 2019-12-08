import telegram
import gsheet

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
		text="Treasurer Bot for Adaptive Network Laboratory Telkom University\n")

def kas(update, context):
    kas_gsheet = gsheet.getKas()
    
    for kas in kas_gsheet:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text="Bayar Kas\n{}".format(kas))