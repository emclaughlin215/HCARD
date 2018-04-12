import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


def send_email():
    fromaddr = "rehapp.data@gmail.com"
    toaddr = "jm4515@ic.ac.uk"


    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "ACL Rehabilitation - Mr. Macabuag Week 1"
    body = "Mr Macabuag completed 7/7 days of rehabilitation.\n Rehapp  "
    msg.attach(MIMEText(body, 'plain'))

    filename = "Data_backend.txt"
    attachment = open("C:\Users\Jacob\Documents\GitHub\HCARD\GUI\Data_backend.txt", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "etienneisbae")
    text = msg.as_string()
    server.sendmail(fromaddr,toaddr, text)
    server.quit()

