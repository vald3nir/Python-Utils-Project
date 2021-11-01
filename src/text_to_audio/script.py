# coding=utf-8
# !/usr/bin/python3

from gtts import gTTS
from playsound import playsound

audio_file = 'audio_test.mp3'
language = 'pt-br'
text = "deu erro na realização do código no windons"

if __name__ == '__main__':
    sp = gTTS(text=text, lang=language, slow=False)
    sp.save(audio_file)
    playsound(audio_file)
