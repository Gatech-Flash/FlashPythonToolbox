# FlashPythonToolbox
A few ready-to use python tools for machine learning

## Logger (to file)
For every print function, we print a copy to file without changing the whole file. 

```
Logger(filepath = "./log.txt", mode = "w", stdout = None)
```
- `filepath`: output path. Default: "./log.txt"
- `mode`: write mode, e.g., w,w+,a,a+. Default: "w"
- `stdout`: capture which print source. Default: "sys.stdout"

Example: 
```
from flashtool import Logger
import sys
sys.stdout = Logger("path/to/log/file/log.txt")
sys.stdout = Logger("path/to/log/file/log.txt","w")
sys.stdout = Logger("path/to/log/file/log.txt","w", sys.stdout)
```

