from email.message import EmailMessage
import smtplib

my_email = EmailMessage()

my_email['from'] = 'Andrew'
my_email['to'] = 'andreiandrewg@gmail.com'
my_email['subject'] = "Hello from Python Lessons!"

my_email.set_content("Hello! How are you doing?")
with smtplib.SMTP(host='localhost', port=2525) as smpt_server:
    smpt_server.ehlo()  # metoda care face legautura cu serverul
    # smpt_server.starttls() # datele shifrovanie
    # smpt_server.login('username','password')
    smpt_server.send_message(my_email)
    print("Email was Sent!!!")
