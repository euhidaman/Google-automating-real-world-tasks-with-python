from email.message import EmailMessage
import getpass
import smtplib
import mimetypes

message = EmailMessage()

sender = input("Enter you email address :")
reciever = input("Enter reciepient's email address : ")
subject = input("Enter subject of message : ")

message['From'] = sender
message['To'] = reciever
message['Subject'] = subject

body = input("Enter body of message : ")

message.set_content(body)

mail_server = smtplib.SMTP_SSL('smtp.gmail.com')

# Make an app password for accessing you email through SMTP
# To know, how to do that for gmail, check out this link ----> https://support.google.com/accounts/answer/185833?hl=en
mail_pass = getpass.getpass('Enter SMTP gmail Password : ')
# the input for the above line will be blank

try:
    mail_server.login(sender, mail_pass)
    print("login successful !!")
    mail_server.send_message(message)
    print("Message sent successfully !!!")
    mail_server.quit()
    print("logout successful !!!")
except:
    print("login unsuccessful !!")
    print("Please try again !!")
