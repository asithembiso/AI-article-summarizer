import os

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

load_dotenv()

SERVICE_ACCOUNT_FILE = "../data/creds/automation.json"
SPREADSHEET_ID = os.getenv("SHEET_ID")
RANGE_NAME = "Sheet1!A:B"


def read_google_sheet():
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
    )
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = (
        sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    )
    values = result.get("values", {})

    if not values:
        print("No data found.")
    return values


data = read_google_sheet()

for items in data:
    print(items)
