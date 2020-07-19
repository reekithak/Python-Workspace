import smtplib
from email.mime.text import MIMEText,MIMEMultipart
username = 'akhilsanker1@gmail.com'
password = '7736313558aA#'

def send_mail(text='Email Body',subject='Hello',from_email='Akhil <akhilsanker1@gmail.com>',to_emails=None):

    assert isinstance(to_emails,list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = to_emails
    msg_str = ""
    #login to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login()
    server.sendmail(from_email,to_emails,msg_str)


    server.quit()
    #with smtplib.SMTP() as server:



    

