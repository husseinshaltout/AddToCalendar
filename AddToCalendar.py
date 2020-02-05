import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
pp = pprint.PrettyPrinter()
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Spring20 Schedule").sheet1

col = sheet.col_values(1)
list_of_hashes = sheet.get_all_records()
header = sheet.row_values(1)
l = sheet.row_values(2)
pp.pprint(header)
pp.pprint(l)

pp.pprint(list_of_hashes[0])

#Date dictionary
dd = {'SUN':'09',
      'MON':'10',
      'TUE':'11', 
      'WED':'12', 
      'THU':'13'}        

#Test dictionary
td = {'': 'SUN',
 '8:30': '',
 '9:30': '',
 '10:30': '',
 '11:30': 'MATH205',
 '12:30': 'MATH205',
 '13:30': '',
 '14:30': 'CSCI221',
 '15:30': 'CSCI221'}
       
for k, v in td.items():
    if(v!= '' and k!=''):        
        title = v        
        start_time = k
        end_time = str(int(start_time[:2]) + 1) + ':' + str(int(start_time[3:]) - 10)
        ddate = dd[list_of_hashes[0]['']]
        print('''Title: %s
              Start: %s 
              End: %s
              Date: 2020-02-%s'''%(title,start_time,end_time,ddate))
        
''' 
#Formating
title = l3[0][1]        
start_time = l3[0][0]
end_time = str(int(start_time[:2]) + 1) + ':' + str(int(start_time[3:]) - 10)
GMT_OFF = '+02:00'
color_id  = 'Basil'
ddate = dd[list_of_hashes[0]['']]         
event = {
        'summary': title,
        'start':{'dateTime':'2020-02-%sT%s:00.000%s'%(ddate,start_time,GMT_OFF)},
        'end':{'dateTime':'2020-02-%sT%s:00.000%s'%(ddate,end_time,GMT_OFF)},
        'recurrence': [
                'RRULE:FREQ=WEEKLY;UNTIL=20200705T170000Z',
                ],
        "colorId": color_id,
        }        
'''

