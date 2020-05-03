'''
Example of how to extract data from a Google Sheet using Google API

Follow instructions to set up the environment here:
https://medium.com/@m.ivhani/setting-up-a-project-service-accounts-and-oauth-credentials-897b35be4175
'''

import json
import smtplib
import gspread
from oauth2client.service_account import ServiceAccountCredentials

 # use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
spr = client.open("icshareholdings")
sheet = spr.worksheet('portfolio')

# Extract and print all of the values
records = sheet.get_all_records()

for item in records:
    print(item)
