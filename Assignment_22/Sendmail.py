# Python code to illustrate sending mail with attachment
# from your Gmail account

# libraries to be imported

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def SendmailwithAttachedment(recieverMailId, fileinfo, mailinfo):
    fromaddr = "kalyanirupeshramteke@gmail.com"
    toaddr = recieverMailId

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # Storing the receiver email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = mailinfo["subject"]

    # string to store the body of the mail
    body = mailinfo["body"]

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = fileinfo["name"]
    filepath = fileinfo["path"] 
    attachement = open(filepath, "rb")

    # instance of MiMEBase and named as P
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachement).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachement; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "password")

    # converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()
