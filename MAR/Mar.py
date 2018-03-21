import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = "marcaestarellas@gmail.com"
toaddr = "marestarellas@gmail.com"


msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL"
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))

filename = "test.pdf"
attachment = open("/Users/davidrockjedeikin/Desktop", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "lapizamarillo")
text = msg.as_string()
server.sendmail(fromaddr,toaddr, text)
server.quit()