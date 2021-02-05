import smtplib
import getpass
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()

sender_mail ='cyril.y@qis.co.in' 
password=getpass.getpass(prompt='Enter your password')
receivers_mail ='cyril.yoh@gmail.com'

s.login(sender_mail,password)

msg='''From: %s
To: %s 
Subject: Sending SMTP e-mail  through python code
This is a test e-mail message sent throgh python code. 
'''%(sender_mail,receivers_mail)

s.sendmail(sender_mail, receivers_mail, msg)

print('mail sent Successfully')
s.quit()
