from email.message import EmailMessage
import os
import smtplib
import mimetypes

message = EmailMessage()

sender = "aman.derax20@gmail.com"
reciever = input("Enter reciepient's email address : ")
subject = input("Enter subject of message : ")

message['From'] = sender
message['To'] = reciever
message['Subject'] = subject

body = input("Enter body of message : ")

message.set_content(body)

mail_server = smtplib.SMTP_SSL('smtp.gmail.com')

mail_pass = os.environ['EMAIL_PASS']

try:
    mail_server.login("aman.derax20@gmail.com", mail_pass)
    print("login successful !!")
    mail_server.send_message(message)
    print("Message sent successfully !!!")
    mail_server.quit()
    print("logout successful !!!")
except:
    print("login unsuccessful !!")
    print("Please try again !!")
