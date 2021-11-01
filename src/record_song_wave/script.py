# coding=utf-8
# !/usr/bin/python3

import sys
import wave

import matplotlib.pyplot as plt
import numpy as np

import subprocess

# =========================================================================================
# RECORD WAVE
# =========================================================================================

quality = "S16_LE"
format = "wav"
device = "hw:1,0"
canal = "1"
rate = "48000"
duration_seconds = "1"
file_name = "wavfile.wav"

print("Recording", file_name)

subprocess.run(["arecord",
                "-f", quality,
                "-t", format,
                "-D", device,
                "-c", canal,
                "-r", rate,
                "-d", duration_seconds,
                file_name])

print("Finish Record", file_name)

# =========================================================================================
# PLOT WAVE
# =========================================================================================

spf = wave.open('wavfile.wav', 'r')
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')

if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)

plt.figure('MOACI')
plt.title('Signal Wave...')
plt.plot(signal[1:])
plt.show()
