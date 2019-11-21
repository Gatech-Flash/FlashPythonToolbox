import smtplib, ssl
from email.mime.text import MIMEText
import json
import os


def checkemail_exists(email):
    try:
        with open(os.path.expanduser('~/.flashtool.email.password'), 'r') as file:
            pwDict = json.load(file)
    except:
        return False
    return email in pwDict.keys()

def setup_email(email):
    password = input("Type your password and press enter will be saved in '~/.flashtool.email.password':")
    try:
        with open(os.path.expanduser('~/.flashtool.email.password'), 'r') as file:
            pwDict = json.load(file)
    except:
        pwDict = {}
    pwDict[email] = password
    with open(os.path.expanduser('~/.flashtool.email.password'), 'w+') as file:
        json.dump(pwDict, file)


def send_email(port = 587,password = None,
        sender_email = "gtflashauto@gmail.com",
        smtp_server="smtp.gmail.com",
        receiver_email = None,
        subject="Subject",
        message="Hello! "):
    """
    import flashtool.email as e
    e.send_email()
    """
    assert receiver_email is not None
    if password is None:
        try:
            with open(os.path.expanduser('~/.flashtool.email.password'), 'r') as file:
                pwDict = json.load(file)
        except:
            pwDict = {}
        if sender_email in pwDict.keys():
            password=pwDict[sender_email]
        else:
            password = input("Type your password and press enter will be saved in '~/.flashtool.email.password':")
            pwDict[sender_email] = password
            with open(os.path.expanduser('~/.flashtool.email.password'), 'w+') as file:
                json.dump(pwDict, file)
    body = """
    {}

    Best,
    GT ISYE FLASH ML GROUP
    """.format(message)
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        # server.ehlo()  # Can be omitted
        server.starttls(context=context)
        # server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
