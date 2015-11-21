#!/usr/bin/python
# insulter.py

import os
import json
import random
import syslog

MY_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DB_DIR = os.getenv('AUDIO_DB_DIR', MY_DIR + "/../insult_db")
AUDIO_DB_FILE = AUDIO_DB_DIR + "/insult_db.json"
AUDIO_DB_FILE_INDEX_ZIELGESCHLECHT = AUDIO_DB_DIR + "/insult_db_index_zielgeschlecht.json"
FILENAME_PATTERN = '/insult{}.aiff'

# play audio with SoX
def play_sound(filename, pitch=0, tempo=1):
    filename = os.path.expanduser(filename)
    print "Playing file ", filename
    #os.system('aplay -D sysdefault:CARD=Device {}'.format(filename))
    cmd = 'play {} pitch {} speed {} bass +3'.format(filename, pitch, tempo)
    print "cmd:", cmd
    os.system(cmd)

class Insulter:

    def __init__(self):

        syslog.openlog('insultr', 0, syslog.LOG_LOCAL4)
        print "MY_DIR={}".format(MY_DIR)
        print "AUDIO_DB_DIR={}".format(AUDIO_DB_DIR)

        if os.path.exists(AUDIO_DB_FILE): 
            with open(AUDIO_DB_FILE) as json_data:
                self.ins_data = json.load(json_data)
                json_data.close()
        if os.path.exists(AUDIO_DB_FILE_INDEX_ZIELGESCHLECHT): 
            with open(AUDIO_DB_FILE_INDEX_ZIELGESCHLECHT) as json_data:
                self.zielgeschlecht2Id = json.load(json_data)
                json_data.close()

    def pickRandom(self, list):
        idx = random.randint(0, len(list) - 1)
        return list[idx], idx 


    def get_insult(self, idx_steig, idx_adj, idx_sub):
        subst, g = self.pickSubstantiv(idx_sub)
        return "Du " + self.pickSteigerung(g, idx_steig) + " " + self.pickAdjektiv(g, idx_adj) + " " + subst


    def speak_next_insult(self, zielgeschlecht, control=0, speed=0):

        id, idx = self.pickRandom(self.zielgeschlecht2Id[zielgeschlecht])
        insult = self.ins_data[str(id)]

        self.log("speaking insult {} from file {}...".format(insult['text'], insult['filename']))
        play_sound(AUDIO_DB_DIR + "/audio" + insult['filename'], control*4, 1+((speed)/200.0))


    def say_hello(self):
        play_sound(AUDIO_DB_DIR + "/audio" + "/hello.aiff")


    def log(self, msg):
        print msg
        syslog.syslog(msg)

if __name__ == "__main__":
    insulter = Insulter()
    #insulter.create_insult_audio_db()

    insulter.speak_next_insult("m")
    insulter.speak_next_insult("f")

