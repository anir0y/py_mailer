import smtplib
import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import os.path
import mimetypes
import random
import string
print ( '''

 _____         __  __       _ _
|  __ \       |  \/  |     (_) |
| |__) |   _  | \  / | __ _ _| | ___ _ __
|  ___/ | | | | |\/| |/ _` | | |/ _ \ '__|
| |   | |_| | | |  | | (_| | | |  __/ |
|_|    \__, | |_|  |_|\__,_|_|_|\___|_|
        __/ |
       |___/
----------------------------- @anir0y --------
'''
)

def randomString(stringLength):

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

email = ("info@hspaceit.com")
#print (email)
f = open("txt.html", "r")
html = f.read()
#file = 'file.pdf'
#html =read(html.txt)
# Read email list txt
email_list = [line.strip() for line in open('email.txt')]
for to_addrs in email_list:
    msg = MIMEMultipart()
    msg['Subject'] = "Join Our New Cyber Security COURSE!"
    msg['From'] = email
    msg['reply-to'] = "mail@domain.tld"
    msg['To'] = to_addrs
    # Attach HTML to the email
    body = MIMEText(html, 'html')
    #attach PDF as Attachment
    msg.attach(body)
    '''
    # Attach PDF to the email
    pdf = MIMEApplication(open("file.pdf", "rb").read())
    pdf.add_header('Content-Disposition', 'attachment', filename="x.pdf")
    msg.attach(pdf)'''


    try:
        server  = smtplib.SMTP('smtp:port') #smtp.mail.com:25
        server.starttls()
        #server.login('user','password')
        server.login('user@domain.tld', 'MailPassw0rd')
        server.sendmail(email,to_addrs, msg.as_string())
        print('msg sent from '+email +' TO  > ' + to_addrs +' Sucess!')
    except:
        print ('Ohh Damn!not working! failed to send: ' + to_addrs)
