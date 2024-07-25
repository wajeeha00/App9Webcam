import smtplib
import imghdr
from email.message import EmailMessage
password = 'smjeaxywujnfcqph'
sender = 'wajeehaaftab7890@gmail.com'
receiver='wajeehaaftab7890@gmail.com'
def send_email(image):
    print('Sending email')
    email_message = EmailMessage()
    email_message['subject'] = 'New Customer'
    email_message.set_content('New customer has arrived')

    with open(image, 'rb') as f:
        content = f.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None,content),
                                  filename='image.png')
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender,receiver, email_message.as_string())
    gmail.quit()
    print('Email sent successfully')

if __name__ == '__main__':
    send_email('images/1.png')
    print('Email sent successfully')

