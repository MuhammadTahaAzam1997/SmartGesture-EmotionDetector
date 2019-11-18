import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import password


sender_email = 'tjbs757@gmail.com'
Reciver_email = 'ms0094449@gmail.com'
Reciver_emails = 'muhammadtahaazam@gmail.com '
Reciver_emailss = 'jahanzi.arif@gmail.com '
Reciver_emailsss = 'Bilalxaeed90@gmail.com  '
password = password.password
subject = 'Suspect Found'
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = Reciver_email
msg['Subject'] = subject

message ='Suspect Person found please be carefull'
msg.attach(MIMEText(message,'plain'))
filename='image.jpg'
attachment=open(filename,'rb')

part = MIMEBase('application','octet_stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('content-Disposition',"attachment; filename= "+filename)
msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('tjbs757@gmail.com',password)
server.sendmail(sender_email,Reciver_email,text)
server.sendmail(sender_email,Reciver_emails,text)
server.sendmail(sender_email,Reciver_emailss,text)
server.sendmail(sender_email,Reciver_emailsss,text)
server.quit()
