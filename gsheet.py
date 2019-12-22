import gspread
import config
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(config.GDRIVE_CRED, scope)
client = gspread.authorize(creds)

# Get spreadsheet by name configured in config.py
# Select specific worksheet you are working on
spreadsheet = client.open(config.GDRIVE_SHEET_NAME)
kas_worksheet = spreadsheet.get_worksheet(3)

def getKas():
    kas_lists = kas_worksheet.get_all_records()
    return kas_lists