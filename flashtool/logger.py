import os,sys

class Logger(object):
    def __init__(self, filepath = "./log.txt", mode = "w", stdout = None):
        if stdout==None:
            self.terminal = sys.stdout
        else:
            self.terminal = stdout
        self.log = open(filepath, mode)

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()
        os.fsync(self.log)

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass

