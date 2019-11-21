import psutil
import time
from .emailutils import checkemail_exists,setup_email,send_email

def trackpid(pid, checktime=1, receiver_email=None, sender_email="gtflashauto@gmail.com", msg=""):
    if not psutil.pid_exists(pid):
        print("Job {} does not exists".format(str(pid)))
        return False
    if receiver_email is not None:
        if not checkemail_exists(sender_email):
            print("Setup Password for {}".format(sender_email))
            setup_email(sender_email)
    msg+="\n Job {} is done".format(str(pid))
    while psutil.pid_exists(pid):
        time.sleep(checktime)
    if receiver_email is not None:
        send_email(receiver_email=receiver_email, sender_email=sender_email, \
            subject="Job {} is done".format(str(pid)), message=msg)
    return True
