import smtplib  #here mail library
import getpass


s = smtplib.SMTP('smtp.gmail.com',587)
# start TLS for security 
s.starttls()

sender_email = "nikhilsamninan@gmail.com"
password = getpass.getpass(prompt="Type your password and press enter: ")
receivers_mail ='nikhilsamninan@gmail.com'

s.login(sender_email,password)

msg='''From: %s
To: %s 
Subject: Sending SMTP e-mail  through python code
This is a test e-mail message sent throgh python code. 
'''%(sender_email,receivers_mail)

s.sendmail(sender_email, receivers_mail, msg)


print('mail sent Successfully')
s.quit()