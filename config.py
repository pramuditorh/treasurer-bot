import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / 'env/.env'
load_dotenv(dotenv_path=env_path)

TELEGRAM_TOKEN = os.getenv("TREASURER_BOT_TELEGRAM_TOKEN")
GDRIVE_CRED = os.getenv("TREASURER_BOT_GDRIVE_CRED")
GDRIVE_SHEET_NAME = os.getenv("TREASURER_BOT_GDRIVE_SHEET_NAME")