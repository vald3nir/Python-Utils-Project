# coding=utf-8
# !/usr/bin/python3

from subprocess import call

libraries = [
    "googletrans==4.0.0-rc1"  # Translate strings
]

call("pip install " + ' '.join(libraries), shell=True)
call("pip freeze > ../../requirements.txt", shell=True)
