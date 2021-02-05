import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

sender_mail = 'cyril.y@qis.co.in'
receiver_mail = 'cyril.yoh@gmail.com'
password = getpass.getpass(prompt='Enter your password: ')

message = MIMEMultipart('alternative')
message['Subject'] = 'HTML mail sent through code'
message['From'] = sender_mail
message['To'] = receiver_mail

msg = '''
<html><body><h1>You are successfully registered to our site</h1>
<a href='https://www.google.com'>Click here</a>
<img src='https://static.toiimg.com/photo/72975551.cms' alt='company logo'>
</body></html>
'''
part = MIMEText(msg,'html')

message.attach(part)


s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(sender_mail,password)
s.sendmail(sender_mail,receiver_mail,message.as_string())
s.quit()