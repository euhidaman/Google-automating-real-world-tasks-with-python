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

x = input("Do you want to add an attachment ? Y/N\n")

if (x == "Y"):
    attachment_path = input("Enter attachment path : \n")
    attachment_filename = os.path.basename(attachment_path)

    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('\',1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype = mime_type,
                               subtype = mime_subtype,
                               filename = os.path.basename(attachment_path))
    print("Sending message.....")

else:
    print("Sending message.....")

mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)

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
