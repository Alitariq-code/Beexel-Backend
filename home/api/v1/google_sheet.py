import gspread
from google.oauth2 import service_account

def google_sheet(options):
    print(options)
    # Specify the path to your JSON key file
    key_path = r'D:\enliven updated\enliven_upskills\home\api\v1\key.json'


    # key_path = '/home/alicode/Desktop/ssh/Enliven/home/api/v1/key.json'
    credentials = service_account.Credentials.from_service_account_file(
        key_path,
        scopes=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    )
    
    # Authenticate with the Google Sheets API
    gc = gspread.authorize(credentials)
    print("Available Spreadsheets:")
    for spreadsheet in gc.list_spreadsheet_files():
        print(spreadsheet['name'], spreadsheet['id'])
    # 1762qBkV22uan0baIEbXr28x6otkjBmqMAZNS5uHnqjw
    # if options["type"]=='apply':
    #  html_content = render_template(options["data"])
    # elif options["type"] == 'contact':
    #    html_content = render_contact_template(options["data"])
    spreadsheet_key = '1OOiG0txEVp8WHQzufxXWX1bWkxRv5HJCXwC2DpzD6pE'
    spreadsheet = gc.open_by_key(spreadsheet_key)
    worksheet = spreadsheet.sheet1
    # resume_url = options['data']['resume_url']
    resume_url = options['data']['resume'].url if options['data']['resume'] else None
    data = [
        options['data']['first_name'],            # First Name
        options['data']['last_name'],             # Last Name
        options['data']['email'],  # Email
        options['data']['phone_no'],   # Position
        options['data']['education'],            # Location
        options['data']['passing_out_year'],       # Phone Number
        options['data']['enroll_course'],        # How Did You Hear
        options['data']['resume'].name if options['data']['resume'] else None,  # Upload CV name
        resume_url  # CV URL
    ]
    worksheet.append_row(data)
#     elif options["type"] == 'contact':
#         spreadsheet_key = '1UsXNSctL4m7EOOPlTmirmzHQSch6ICzxstUd3iGPirA'
#         spreadsheet = gc.open_by_key(spreadsheet_key)
#         worksheet = spreadsheet.sheet1
#         data = [
#     options['data']['full_name'],    # Full Name
#     options['data']['email'],        # Email
#     options['data']['subject'],      # Subject
#     options['data']['message'],      # Message
# ]
#         worksheet.append_row(data)