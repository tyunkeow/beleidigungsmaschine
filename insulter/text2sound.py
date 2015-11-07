import os
import sys
import base64
import time


DEFAULT_VOLUME = 50
DEFAULT_SPEED = 1
AUDIO_DIR = os.path.dirname(os.path.abspath(__file__)) + '/data/audio/'

def text2soundfile(text, filename, overwrite=False):
    filename = os.path.expanduser(filename)
    file_exists = os.path.exists(filename)
    if not overwrite and file_exists:
        print "Soundfile {} already exists and overwrite flag was not set. Skipping...".format(filename)
    else:
        text2aiff_mac(text, filename)


# play audio with SoX
def play_sound(filename, pitch=0, tempo=1):
    filename = os.path.expanduser(filename)
    print "Playing file ", filename
    #os.system('aplay -D sysdefault:CARD=Device {}'.format(filename))
    cmd = 'play {} pitch {} speed {} bass +3'.format(filename, pitch, tempo)
    print "cmd:", cmd
    os.system(cmd)
