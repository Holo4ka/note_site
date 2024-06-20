import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
addr_from = "ighor1544@gmail.com"                 # Адресат
password = "quxn kbhn dtxi pizd"

addr_to = "ighor1544@gmail.com"                   # Получатель

msg = MIMEMultipart()                             # Создаем сообщение
msg['From'] = addr_from                           # Адресат
msg['To'] = addr_to                               # Получатель
msg['Subject'] = 'Greeting'                       # Тема сообщения
body = "Hello World"

msg.attach(MIMEText(body, 'plain'))

smtpObj.login(addr_from, password)
smtpObj.send_message(msg)
smtpObj.quit()


def send_message(to_add, subj, message):
    global addr_to, password

    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = addr_from  # Адресат
    msg['To'] = to_add  # Получатель
    msg['Subject'] = subj  # Тема сообщения
    body = message

    msg.attach(MIMEText(body, 'plain'))

    smtpObj.login(addr_from, password)
    smtpObj.send_message(msg)
    smtpObj.quit()

'''smtpObj.login("ighor1544@gmail.com", "quxn kbhn dtxi pizd")

smtpObj.sendmail("ighor1544@gmail.com", "ighor1544@gmail.com", "Hello World")

smtpObj.quit()
'''
