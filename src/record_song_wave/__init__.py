# coding=utf-8
# !/usr/bin/python3

from subprocess import call

libraries = [
    "matplotlib", 
    "numpy"
]

call("pip install " + ' '.join(libraries), shell=True)
call("pip freeze > ../../requirements.txt", shell=True)
