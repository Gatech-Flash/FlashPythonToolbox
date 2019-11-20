import psutil

def check_pid(pid, checktime=1, receiver_email=None, msg=""):
    msg+="\n job {} is done".format()
