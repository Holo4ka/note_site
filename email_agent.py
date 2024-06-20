import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()

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
