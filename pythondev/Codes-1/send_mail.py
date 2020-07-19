import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
username = 'akhilsanker1@gmail.com'
password = 'typo?#'

def send_mail(text='Email Body',subject='Hello',from_email='Akhil <akhilsanker1@gmail.com>',to_emails=None,html=None):

    assert isinstance(to_emails,list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ','.join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text,'plain')
    msg.attach(txt_part)

    html_part = MIMEText('<h1>This is a working space </h1>','html')
    if html!=None:
        msg.attach(html_part)
    else:
        pass
    msg_str = msg.as_string()
    #login to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)


    server.quit()
    #with smtplib.SMTP() as server:



    

