import psutil
import time
from .emailutils import checkemail_exists,setup_email,send_email
import copy

def trackpid(pid, checktime=1, receiver_email=None, sender_email="gtflashauto@gmail.com", msg=""):
    if not isinstance(pid,list):
        pid = [pid]
    for id in pid:
        if not psutil.pid_exists(id):
            print("Job {} does not exists".format(str(id)))
            return False
    if receiver_email is not None:
        if not checkemail_exists(sender_email):
            print("Setup Password for {}".format(sender_email))
            setup_email(sender_email)
    while len(pid) > 0:
        removed_pid = [id for id in pid if not psutil.pid_exists(id)]
        if receiver_email is not None:
            for id in removed_pid:
                send_email(receiver_email=receiver_email, sender_email=sender_email, \
                    subject="Job {} is done".format(str(id)), \
                    message="{}\n Job {} is done".format(msg, str(id)))
        pid = [id for id in pid if id not in removed_pid]
        time.sleep(checktime)
    return True
