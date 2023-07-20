import smtplib
import ssl
import os
from email.message import EmailMessage

# Define email sender and receiver
email_sender = '{insert email here}}'
email_password = '{insert password here}'
email_receiver_file = '{insert file here }'  # Name of the file containing email addresses
cc_email = '{insert cc here}'  # Replace with the actual CC email address

# Set the subject of the email
subject = 'insert subject here'

# HTML template for the email body
body_template = """
<html>
<head>
    <title></title>
    
</head>
<body>
    <p>Dear {insert name here},</p>
    <p>insert body here</p>
</html>
"""

import re

def extract_emails_from_file(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Regular expression pattern to find email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all matches of email addresses in the file content
    emails = re.findall(pattern, file_content)

    # Remove duplicates and return the list of unique email addresses
    unique_emails = list(set(emails))

    return unique_emails

# Replace 'file_path' with the actual path to your file
file_path = 'insert file path here'

# Call the function with the file path to get the list of email addresses
email_addresses = extract_emails_from_file(file_path)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email to each receiver
for email_receiver in email_addresses:
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em['CC'] = cc_email

    # Set the email body as HTML content
    em.set_content(body_template, subtype='html')

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        recipients = [email_receiver]
        if cc_email:
            recipients.append(cc_email)
        smtp.sendmail(email_sender, recipients, em.as_string())
        print(f'Email sent successfully to {email_receiver}!')

print('All emails sent successfully!')
