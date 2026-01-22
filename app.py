import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION ---
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def prepare_email(subject, sender_email, receiver_email, message, files=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # 1. Update body text if files exist
    body = message
    if files:
        body += "\n\nPlease find the attached file(s)."

    # 2. Set content FIRST
    msg.set_content(body)

    # 3. Add attachments SECOND
    if files:
        for file in files:
            try:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(file)
                msg.add_attachment(
                    file_data,
                    maintype='application',
                    subtype='octet-stream',
                    filename=file_name
                )
            except Exception as e:
                print(f"Failed to attach {file}: {e}")

    return msg


def connect_smtp(sender_email, app_password):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        return server
    except Exception as e:
        print(f"Failed to connect to SMTP server: {e}")
        return None


def send_mail(emails: list[EmailMessage], sender_email, password):
    server = connect_smtp(sender_email, password)
    if not server:
        return

    try:
        for email in emails:
            try:
                # Persistent connection: send all messages in one session
                server.send_message(email)
                print(f"Success: '{email['Subject']}' sent to {email['To']}")
            except Exception as e:
                print(f"sending '{email['Subject']}': {e}")
    finally:
        # Gracefully close connection after all emails are processed
        server.quit()
        print("SMTP Connection closed.")


# --- HOW TO RUN IT ---
if __name__ == "__main__":
    # Create a list of email objects
    file_paths = [r"C:\Users\Admin\Desktop\picture1.jpg",
                  r"C:\Users\Admin\Desktop\picture2.jpg"]
    my_emails = [
        prepare_email("Report 1", SENDER_EMAIL, "xyz@email.com",
                      "Here is report 1", file_paths),
        prepare_email("Update 2", SENDER_EMAIL,
                      "xyz@email.com", "Just an update", None)
    ]

    # Send them all over one connection
    send_mail(my_emails, SENDER_EMAIL, APP_PASSWORD)
