import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# start the process
server.ehlo()

# log in
with open('credentials.txt', 'r') as file:
  emailFrom = file.readline()
  password = file.readline()
  emailTo = file.readline()

server.login(emailFrom, password)

# email
msg = MIMEMultipart()
msg['From'] = emailFrom
msg['To'] = emailTo
msg['Subject'] = 'Email de Prueba'

# message
with open('message.txt', 'r') as file:
  message = file.read()

msg.attach(MIMEText(message, 'plain'))

# image
filename = 'python-email.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
attachment.close()

# send
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail(emailFrom, emailTo, text)

server.quit()

