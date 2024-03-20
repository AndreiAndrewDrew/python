from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

my_email = EmailMessage()

html_template = Template(Path("templates/index.html").read_text())
html_content = html_template.substitute({'name': 'Andrew','date': 'tomorrow'})


my_email['from'] = 'Andrew'
my_email['to'] = 'friend@gmail.com'
my_email['subject'] = "Hello from Python2 Lessons2!"
my_email.set_content(html_content, 'html')

with smtplib.SMTP(host='localhost', port=2525) as smpt_server:
    smpt_server.ehlo()  # metoda care face legautura cu serverul
    # smpt_server.starttls() # datele shifrovanie
    # smpt_server.login('username','password')
    smpt_server.send_message(my_email)
    print("Email was Sent!!!")
