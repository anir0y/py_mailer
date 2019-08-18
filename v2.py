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
#impors are important don't delete 'em if you don't understat what they are!
#padding done here:
def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
email = ("accounts"+randomString(8)+"@earth.space")
#print (email)
#uncheck this #file if you need attachments
#file = 'int.doc'
html = """

<center> your HTML code here</center>

"""
# Read email list txt
email_list = [line.strip() for line in open('email.txt')]
for to_addrs in email_list:
    msg = MIMEMultipart()
    msg['Subject'] = "Subject!"
    msg['From'] = email
    msg['To'] = to_addrs
    # Attach HTML to the email
    #body = MIMEText(html, 'html')
    #msg.attach(body)
    #'''
    # Attach PDF to the email
    #pdf = MIMEApplication(open("x.pdf", "rb").read())
    #pdf.add_header('Content-Disposition', 'attachment', filename="x.pdf")
    #msg.attach(pdf)'''
    #docFinallyWorking
    #fp = open(file, 'rb')
    #part = MIMEBase('application', 'vnd.ms.word')
    #part.set_payload(fp.read())
    #fp.close()
    #encoders.encode_base64(part)
    #part.add_header('Content-Disposition','attachment',filename='int.doc')
    #msg.attach(part)
    #'''
    #xlsx
    #fp = open(file,'rb')
    #part = MIMEBase('application','vnd.ms-excel')
    #part.set_payload(fp.read())
    #fp.close()
    #encoders.encode_base64(part)
    #part.add_header('Content-Disposition','attachment', filename="int.xlsx")
    #msg.attach(part)'''
    try:
        #smtp config :
        server  = smtplib.SMTP('smtp.server:port') #(smtp.gmail.com:25)
        server.starttls()
        #server.login('user','password')
        server.login('mail@user.tld', 'mailPassword') # ('me@mail.com', 'password')
        server.sendmail(server,to_addrs, msg.as_string())
        print('msg sent from '+email +' TO  > ' + to_addrs +' Sucess!')
    except:
        print ('Ohh Damn!not working! failed to send: ' + to_addrs)
