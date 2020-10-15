# FlashPythonToolbox
A few ready-to use python tools for machine learning

## Install
```
pip install flashtool
```

## Logger (to file)
For every print function, we print a copy to file without changing the whole file.

```python
Logger(filepath = "./log.txt", mode = "w", stdout = None)
```
- `filepath`: output path. Default: "./log.txt"
- `mode`: write mode, e.g., w,w+,a,a+. Default: "w"
- `stdout`: capture which print source. Default: "sys.stdout"

Example:
```python
from flashtool import Logger
import sys
sys.stdout = Logger("path/to/log/file/log.txt")
sys.stdout = Logger("path/to/log/file/log.txt","w")
sys.stdout = Logger("path/to/log/file/log.txt","w", sys.stdout)
```

## Email Module

Default Sender: `gtflashauto@gmail.com`. You need a password for this.

```python
# Function api
def send_email(port = 587,password = None,
        sender_email = "gtflashauto@gmail.com",
        smtp_server="smtp.gmail.com",
        receiver_email = None,
        subject="Subject",
        message="Hello! ",
        attachment=None):
    ...

# Example
from flashtool import send_email
send_email(receiver_email="xxx@gmail.com", subject="Hi", message="first email")
```

## Track Job

Track your job. Send you an email when it is done.

**Tracking by PID**
- Step 1: find your job pid by `ps`, e.g., `ps aux | grep python`
- Step 2:
```python
from flashtool import trackpid
trackpid(12345,5,"xxx@gmail.com")
trackpid([1357,2468],5,"xxx@gmail.com")
```
*API*:
```python
def trackpid(pid, checktime=1, receiver_email=None, sender_email="gtflashauto@gmail.com", msg=""):
  ...
```
- `pid`: pid or pids
- `checktime`: check pid every `checktime` seconds
- `msg`: additional message

## Pytorch Utils

### GPU Usage

```python
import flashtool as flash; flash.check_torch_memory(brief=True)
```
- `brief`: short message (default: Flase)


## Auto Script Running

```python
import flashtool as flash;
basescript='script/run.sh'
config={
    "DATA": "subset5"
}
flash.run_script(basescript, config)
```

## Profile Timing Line by Line 

```python

from flashtool import line_time_profiler 

@line_time_profiler()
def f(n=1000):
    a = [1 for _ in range(n)]
    b = sum(a)

f()
f(10000)

class C:
    @line_time_profiler()
    def f(self, n=1000):
        a = [1 for _ in range(n)]
        b = sum(a)

ins = C()
ins.f()
ins.f(10000)


@line_time_profiler(stop=True)
def f(n=1000):
    a = [1 for _ in range(n)]
    b = sum(a)

f()

```
