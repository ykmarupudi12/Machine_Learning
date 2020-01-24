import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Krishna.Marupudi@live.com'
email['to'] = 'ykmarupudi@icloud.com'
email['subject'] = 'from my python script'
email.set_content('Hi this message is sent from my python script')
with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('krishna.marupudi@live.com', 'Y@mini1260')
    smtp.send_message(email)
    print('message sent')
