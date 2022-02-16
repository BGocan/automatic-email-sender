from calendar import c
from http import server
import smtplib #Simple Mail Transfer Protocol
import ssl #Secure Sockets Layer
from email.message import EmailMessage

receiver_list = ["megarjonny@gmail.com"]

subject = "Hello World!"
body = input("Enter message here: ")
sender_email = "protoemailerautomated@gmail.com"
receiver_email = receiver_list[0]
password = "mLIMVkBv^"

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email...")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")