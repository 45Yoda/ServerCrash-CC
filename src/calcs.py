import subprocess
import re

def memAv():
    out = subprocess.check_output("free -m",shell=True)
    lol = re.findall("Mem:\s{1,}.*\s{1,}([0-9].*)",out.decode())

    return lol[0]

def load():
    out = subprocess.check_output("uptime",shell=True)
    lol = re.findall("[0-9]\.[0-9]+",out.decode());

    return lol[2]
