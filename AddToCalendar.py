import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pprint
pp = pprint.PrettyPrinter()
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Spring20 Schedule").sheet1



scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("client_secret1.json", scopes=scopes)
credentials = flow.run_console()

CAL = build("calendar", "v3", credentials=credentials)

list_of_hashes = sheet.get_all_records()
pp.pprint(list_of_hashes[0])

#Date dictionary
dd = {'SUN':'09',
      'MON':'10',
      'TUE':'11', 
      'WED':'12', 
      'THU':'13'}        
#Color id dictionary
cid = {'CSCI221':'Peacock',
       'CSCI221T2':'Peacock',
       'CSCI221L1':'Peacock',
       'MATH205':'Basil',
       'MATH205T2':'Basil',
       'CSCI463':'Tomato',
       'CSCI463T':'Tomato',
       'CSCI463L':'Tomato',
       'CSCI467':'Banana',
       'CSCI467T':'Banana'}
def setEvent(list_of_hashes,dd,cid):
    GMT_OFF = '+02:00'
    for i in range(len(list_of_hashes)):
        print("***%s"%list_of_hashes[i][''])
        for k, v in list_of_hashes[i].items():
            if(v!= '' and k!=''):        
                title = v        
                start_time = k
                end_time = str(int(start_time.split(':')[0]) + 1) + ':' + str(int(start_time.split(':')[1]) - 10)
                ddate = dd[list_of_hashes[i]['']]
                color_id = cid[title]
                print('''Title: %s
                      Start: %s 
                      End: %s
                      Date: 2020-02-%s
                      Color: %s'''%(title,start_time,end_time,ddate,color_id))
                return title, start_time, end_time, ddate, color_id
    
      
#Test
title = 'MATH205Test'
start_time = '10:30'
end_time = '11:30'
ddate = dd[list_of_hashes[0]['']]
color_id = cid['MATH205']
#Event Format
GMT_OFF = '+02:00'  
event = {
        'summary': title,
        'start':{'dateTime':'2020-02-%sT%s:00.000%s'%(ddate,start_time,GMT_OFF),'timeZone': 'Africa/Cairo'},
        'end':{'dateTime':'2020-02-%sT%s:00.000%s'%(ddate,end_time,GMT_OFF),'timeZone': 'Africa/Cairo'},
        'recurrence': ['RRULE:FREQ=WEEKLY;UNTIL=20200216T170000Z',]}        
recurring_event = CAL.events().insert(calendarId='primary', body=event).execute()

print('''*** %s event added:
    Start: %s
    End: %s'''%(recurring_event['summary'],
    recurring_event['start']['dateTime'],recurring_event['end']['dateTime']))


