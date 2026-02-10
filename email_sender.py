import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from secrets import sender_email, receiver_email, password

# Email details
sender_email = "4mh23cs019@gmail.com"
receiver_email = "bhoomibhoomi7795@gmail.com"
password = "wyan bnqd wiot keio"

subject = "Test Email from Python"
body = "Hello! This email was sent using Python."

# Create email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Send email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # secure connection
    server.login(sender_email, password)
    server.send_message(msg)

print("Email sent successfully!")
