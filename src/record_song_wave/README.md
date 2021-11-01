# Record Song Wave
Python script to record and plot the music wave from the audio card

## ALSA LIB

    sudo apt-get install build-essential libasound2-dev -y

## Setup Audio Board

sudo nano /etc/asound.conf

    pcm.!default {
            type hw
            card 1
    }
    ctl.!default {
            type hw
            card 1
    }