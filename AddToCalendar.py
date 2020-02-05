import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
pp = pprint.PrettyPrinter()
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Spring20 Schedule").sheet1

col = sheet.col_values(3)
list_of_hashes = sheet.get_all_records()
header = sheet.row_values(1)
l = sheet.row_values(2)
pp.pprint(header)
pp.pprint(l)

pp.pprint(list_of_hashes[0])
            
                
l3 = []            
counter = 0
for k, v in list_of_hashes[0].items():
    if(v!= '' and k!=''):        
#        l3.append([k])
#        l3[counter].append(v)
#        counter += 1
        print(k, v)
       
#Formating
title = l3[0][1]        
start_time = l3[0][0]
end_time = str(int(start_time[:2]) + 1) + ':' + str(int(start_time[3:]) - 10)
GMT_OFF = '+02:00'        
event = {
        'summary': title,
        'start':{'dateTime':'2020-02-09T%s:00.000%s'%(start_time,GMT_OFF)},
        'end':{'dateTime':'2020-02-09T%s:00.000%s'%(end_time,GMT_OFF)},
        'recurrence': [
                'RRULE:FREQ=WEEKLY;UNTIL=20200705T170000Z',
                ]
        }        