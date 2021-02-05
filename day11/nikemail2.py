import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
sender_mail = 'nikhilsamninan@gmail.com'
receiver_mail = 'nikhilsamninan@gmail.com'
password = getpass.getpass(prompt='Enter your password: ')

message = MIMEMultipart('alternative')
message['Subject'] = 'HTML mail sent through code'
message['From'] = sender_mail
message['To'] = receiver_mail

msg = '''
<html><body><h1>You are successfully registered to our site</h1>
<a href='https://www.google.com'>Click here</a>
<img src='https://i.pinimg.com/564x/83/f9/37/83f937b69f30bb886ab8a03390da6771.jpg' alt='company logo'>
</body></html>
'''
part = MIMEText(msg,'html')

message.attach(part)


s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(sender_mail,password)
s.sendmail(sender_mail,receiver_mail,message.as_string())
print("Email send successfully")
s.quit()