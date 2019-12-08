import telegram

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
		text="Treasurer Bot for Adaptive Network Laboratory Telkom University\n")