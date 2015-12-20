#!/usr/bin/python
# insulter.py

import os
import json
import random
import logging

MY_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DB_DIR = os.getenv('AUDIO_DB_DIR', MY_DIR + "/../insult_db")
AUDIO_DB_FILE = AUDIO_DB_DIR + "/insult_db.json"
AUDIO_DB_FILE_INDEX_ZIELGESCHLECHT = AUDIO_DB_DIR + "/insult_db_index_zielgeschlecht.json"
FILENAME_PATTERN = '/insult{}.ogg'

# play audio with SoX
def play_sound(filename, pitch=0, tempo=1):
    filename = os.path.expanduser(filename)
    cmd = 'play {} pitch {} speed {} bass +3 &'.format(filename, pitch, tempo)
    logging.info("play_sound(): cmd: {}".format(cmd))
    os.system(cmd)

class Insultr:
    ins_data = None
    zielgeschlecht2Id = None
    zielgeschlecht = 'f' # can be 'f' or 'm'
    last_substantiv = None
    last_adjektiv = None
    last_steigerung = None

    def __init__(self):
        self.log("Insultr(): MY_DIR={}".format(MY_DIR))
        self.log("Insultr(): AUDIO_DB_DIR={}".format(AUDIO_DB_DIR))

        self.log("Insultr(): Opening {} ...".format(AUDIO_DB_FILE))
        with open(AUDIO_DB_FILE) as json_data:
            self.ins_data = json.load(json_data)
            json_data.close()
        
        self.log("Insultr(): Opening {} ...".format(AUDIO_DB_FILE_INDEX_ZIELGESCHLECHT))
        with open(AUDIO_DB_FILE_INDEX_ZIELGESCHLECHT) as json_data:
            self.zielgeschlecht2Id = json.load(json_data)
            json_data.close()

    def pickRandom(self, list):
        idx = random.randint(0, len(list) - 1)
        return list[idx], idx 

    def speak_next_insult(self, control=0, speed=0):

        # The simplest thing that could possibly work... TODO use a 'real' database
        while True:
            id, idx = self.pickRandom(self.zielgeschlecht2Id[self.zielgeschlecht])
            insult = self.ins_data[str(id)]
            if not insult['substantiv'] == self.last_substantiv:
                break

        self.last_substantiv = insult['substantiv']
        self.last_adjektiv = insult['adjektiv']
        self.last_steigerung = insult['steigerung']

        self.log("speaking insult {} from file {}...".format(insult['text'], insult['filename']))
        play_sound(AUDIO_DB_DIR + "/audio" + insult['filename'], control*4, 1+((speed)/200.0))


    def say_hello(self):
        play_sound(AUDIO_DB_DIR + "/audio" + "/hello.ogg")

    def set_maennlich(self):
        play_sound(AUDIO_DB_DIR + "/audio" + "/ModusMaennlich.ogg")
        self.zielgeschlecht = 'm'

    def set_weiblich(self):
        play_sound(AUDIO_DB_DIR + "/audio" + "/ModusWeiblich.ogg")
        self.zielgeschlecht = 'f'


    def log(self, msg):
        print msg
        logging.info(msg)

if __name__ == "__main__":
    #logging.basicConfig(filename='/var/log/insultr.log',level=logging.DEBUG)
    insultr = Insultr()
    #insulter.create_insult_audio_db()

    insultr.set_weiblich()
    insultr.speak_next_insult()
    insultr.set_maennlich()
    insultr.speak_next_insult()

