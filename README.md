# AddToCalendar
A script to add my schedule from google sheets to google calendar using google APIs
![ref](https://user-images.githubusercontent.com/48390004/73819906-3338a300-47f9-11ea-9029-289142bdf4af.png)
## Getting Started
To access your spreadsheet, you’ll need to create a service account and OAuth2 credentials from the Google API Console
- Go to the Google APIs Console.
- Create a new project.
- Click Enable API. Search for and enable the Google Drive API.
- Create credentials for a Web Server to access Application Data.
- Name the service account and grant it a Project Role of Editor.
- Download the JSON file.
- Copy the JSON file to your code directory and rename it to client_secret.json
- Find the  client_email inside client_secret.json. Back in your spreadsheet, click the Share button in the top right, and paste the client email into the People field to give it edit rights. Hit Send.
#### OAuth Client ID
- Go to https://console.developers.google.com/apis/credentials
- Create credentials  
- OAuth Client ID
- Other
- Create OAuth consent screen 
- Just add a name and save
- Download the JSON file.
- Copy the JSON file to your code directory and rename it to client_secret1.json

## Prerequisites
- pip install google-api-python-client
- pip install gspread oauth2client
### To be changed
- replace SHEET NAME in `sheetName = "SHEET NAME"` with your google sheet name
- change event starting dates in the date dictionary part `dd = {'SUN':'2020-02-09'` the date format: yyyy-mm-dd
- `cid = {'Course 1':'9',}` choose course name and color id for the event color
- `GMT_OFF = '+02:00'` and `'timeZone': 'Africa/Cairo'` adjust accourding to your timezone
