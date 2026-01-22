Python Gmail SMTP Automator
A robust, modular Python script for automating email delivery using Gmail's SMTP server. This project is designed for efficiency, using a single persistent connection to send multiple emails with attachments.

🚀 Features
Modular Design: Separate functions for email preparation, SMTP connection, and batch sending.

Secure: Uses python-dotenv to keep credentials out of the source code.

Efficient: Opens one SMTP connection to send multiple emails, reducing overhead.

Attachments: Supports sending multiple files (PDFs, images, etc.) per email.

🛠️ Prerequisites
Python 3.x

App Password: Generate a 16-character password from your Google Account Security settings.

2-Step Verification: Must be enabled on your Google account.

📦 Setup
Clone the repository:

Bash
git clone https://github.com/yourusername/gmail-automation.git
cd gmail-automation
Install dependencies:

Bash
pip install python-dotenv
Create a .env file in the root directory:

Plaintext
SENDER_EMAIL=your-email@gmail.com
APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
🖥️ Usage
Import the functions and pass a list of prepared EmailMessage objects to the send_mail function.

Python
from app import prepare_email, send_mail

# Prepare emails
emails = [
    prepare_email("Subject", "sender@gmail.com", "receiver@gmail.com", "Hello World!", ["file.pdf"])
]

# Send batch
send_mail(emails, SENDER_EMAIL, APP_PASSWORD)
