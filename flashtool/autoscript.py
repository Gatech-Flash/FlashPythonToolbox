import os, sys
import subprocess

def replace(script, key, value):
    key = str(key)
    value = str(value)
    startid = script.find("\n" + key + "=")
    startid += 1
    assert script[startid - 1] == "\n"
    endid = script.find("\n", startid)
    print("Replacing|{}|==>|{}|".format(script[startid:endid], key + "=" + value))
    newscript = script[:startid] + key + "=" + value + script[endid:]
    return newscript


def run_script(basescript, replace_dict={}):
    print("==================BEGIN===================")
    try:
        with open(basescript, mode="r") as f:
            _script = f.read()
        for k, v in replace_dict.items():
            _script = replace(_script, k, v)
        print("cwd: ", os.path.abspath("."))
        subprocess.run([_script, basescript], shell=True, cwd=os.path.abspath("."))
    except:
        print("==================FAILED==================")
        print(basescript)
        print(replace_dict)
    print("====================END===================")
    print("\n\n")
