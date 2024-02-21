import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def render_template(context):
    base_url = 'http://beexcel.ai:8003/'
    resume_url_html = ''

    # try:
    #     if context['resume']:
    #         resume_url_html = f'<p><strong>Resume:</strong> <a href="{base_url}{context["resume"].url}" download="{context["resume"].name}">{context["resume"].name}</a></p>'
    # except Exception as e:
    #     print(f"Error generating resume URL HTML: {e}")
    
   
    resume_url_html = '' if not context['resume'] else f'<p><strong>Resume URL:</strong> <a href="{base_url}{context["resume_url"]}" target="_blank">{context["resume_url"]}</a></p>'
   
    template = f"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Course Application Details - enlivenAi</title>
        <style>
          body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #F5F5F5;
            color: #333;
          }}
          h1 {{
            color: #007BFF;
          }}
          p {{
            margin-bottom: 15px;
          }}
          strong {{
            font-weight: bold;
          }}
          a {{
            color: #007BFF;
            text-decoration: none;
          }}
          a:hover {{
            text-decoration: underline;
          }}
        </style>
      </head>
      <body>
        <h1>Course Application Details - enlivenAi</h1>
        <p><strong>First Name:</strong> {context['first_name']}</p>
        <p><strong>Last Name:</strong> {context['last_name']}</p>
        <p><strong>Email:</strong> {context['email']}</p>
        <p><strong>Phone Number:</strong> {context['phone_no']}</p>
        <p><strong>Education:</strong> {context['education']}</p>
        <p><strong>Passing Out Year:</strong> {context['passing_out_year']}</p>
        <p><strong>Enroll Course:</strong> {context['enroll_course']}</p>
        {resume_url_html}

      </body>
    </html>
    """
    return template

# def render_contact_template(context):
#     template = f"""
#     <!DOCTYPE html>
#     <html lang="en">
#       <head>
#         <meta charset="UTF-8" />
#         <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#         <title>Contact Us Details - enlivenAi</title>
#         <style>
#           body {{
#             font-family: Arial, sans-serif;
#             line-height: 1.6;
#             margin: 20px;
#             padding: 20px;
#             background-color: #F5F5F5;
#             color: #333;
#           }}
#           h1 {{
#             color: #007BFF;
#           }}
#           p {{
#             margin-bottom: 15px;
#           }}
#           strong {{
#             font-weight: bold;
#           }}
#           a {{
#             color: #007BFF;
#             text-decoration: none;
#           }}
#           a:hover {{
#             text-decoration: underline;
#           }}
#         </style>
#       </head>
#       <body>
#         <h1>Contact Us Details - enlivenAi</h1>
#         <p><strong>Full Name:</strong> {context['full_name']}</p>
#         <p><strong>Email:</strong> {context['email']}</p>
#         <p><strong>Subject:</strong> {context['subject']}</p>
#         <p><strong>Message:</strong> {context['message']}</p>
#       </body>
#     </html>
#     """
#     return template

# def send_email(options):
#     # Set up the SMTP server
#     smtp_host = 'smtp.gmail.com'
#     smtp_port = 587
#     smtp_username = 'nosheenbu1@gmail.com'
#     smtp_password = 'aypl tfoy ncnm xvaw'
#     send_to = 'haseeb.bhp@gmail.com'

#     # Create an EmailMessage instance
#     subject = 'Notification'
#     from_email = 'Nosheen <nosheenbu1@gmail.com>'
#     to_email = ['hamza@enlivensai.com']  # Use a list for multiple recipients
#     text_content = 'This is a plain text message.'

#     # Use the Django template system to render the HTML content
#     if options["type"] == 'apply':
#         html_template = render_template(options)
#         print("html_template", html_template)

#         html_content = html_template.render(Context({}))  # Add context if needed
#     else:
#         html_content = ''

#     # Create the EmailMessage instance with both text and HTML content
#     msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
#     msg.attach_alternative(html_content, 'text/html')

#     # Set up the SMTP connection
#     msg.connection = get_connection(host=smtp_host, port=smtp_port, username=smtp_username, password=smtp_password)

#     # Send the email
#     msg.send()

#     print('Email sent successfully!')




def send_email(options):
    # Set up the SMTP server
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'nosheenbu1@gmail.com'
    smtp_password = 'aypl tfoy ncnm xvaw'
    send_to='enlivenembeddedtech@gmail.com'
    # Create a connection to the SMTP server
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    print(options)
    # # Log in to the SMTP server
    server.login(smtp_username, smtp_password)
    html_content=''
    if options["type"]=='apply':
     html_content = render_template(options["data"])
    # elif options["type"] == 'contact':
    #    html_content = render_contact_template(options["data"])
    msg = MIMEMultipart()
    msg['From'] = 'Nosheen <nosheenbu1@gmail.com>'
    msg['To'] = 'hamza@enlivensai.com'
    msg['Subject'] = 'Notification'
    print(send_to)
    # # Attach the HTML message body
    msg.attach(MIMEText(html_content, 'html'))
    # # Send the email
    server.sendmail(smtp_username, 'enlivenembeddedtech@gmail.com', msg.as_string())
    # # Quit the SMTP server
    server.quit()
    print('Email sent successfully!')
