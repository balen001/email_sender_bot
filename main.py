import smtplib

sender = 'balenahmed70@gmail.com'
receiver = 'balen.ahmed@ukh.edu.krd'
password = 'huakxjsyaanumkij'
subject = 'python email test'
body = "Hello world, I am here"


#header

message = f""" From: Balen{sender}
To: {receiver}
Subject: {subject}\n
{body}

"""

#Gmail SMTP port (TLS): 587
#Gmail SMTP port (SSL): 465
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() #To start a transport layer security to establish a secure connection 
    server.login(sender, password)
    print("logged in")
    server.sendmail(sender, receiver, message)
    print("Email successfuly sent")
except smtplib.SMTPAuthenticationError:
    print("Wrong email or password")

