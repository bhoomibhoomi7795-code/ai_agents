import smtplib
from email.message import EmailMessage
from secrets import sender_email, receiver_email, password

# Email details
def send_email(receiver_email,subject,content):
   
# Create email
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(content)

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # secure connection
        server.login(sender_email, password)
        server.send_message(msg)

    print("Email sent successfully!")

send_email("bhoomibhoomi7795@gmail.com","Test Email from Python","Hello! This email was sent using Python.")