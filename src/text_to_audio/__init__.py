# coding=utf-8
# !/usr/bin/python3

from subprocess import call

libraries = [
    "gtts",  # text to audio
    "playsound",  # play audio
]

call("pip install " + ' '.join(libraries), shell=True)
call("pip freeze > ../../requirements.txt", shell=True)
