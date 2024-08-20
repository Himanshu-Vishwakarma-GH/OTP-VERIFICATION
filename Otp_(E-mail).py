import random
import smtplib
from email.message import EmailMessage

otp = ""
for i in range (6):
    otp += str(random.randint(0,9))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

from_mail = 'himanshuvishwakarma516@gmail.com'
server.login(from_mail,'#App Password#')
to_mail = input("Enter Your E-Mail:")

msg = EmailMessage()
msg['Subject'] = "OTP Verification"
msg['From'] = from_mail
msg['To'] = to_mail
msg.set_content("Your OTP Is:" +otp)

server.send_message(msg)
print("OTP Is Mailed To Respective ")

a=input("Enter The OTP: ")

if a==otp:
    {
    print("OTP is Verified")
}
else:{
    print("Wrong OTP Entered")
}
