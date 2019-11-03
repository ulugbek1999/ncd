import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings


def send_gspread(data):
    credentials = ServiceAccountCredentials.from_json_keyfile_name('utils/credentials.json', settings.SCOPE)
    gc = gspread.authorize(credentials)
    wks = gc.open('NCD').sheet1
    wks.append_row(data)