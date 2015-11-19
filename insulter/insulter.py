#!/usr/bin/python
# insulter.py

import os
import json
import random
import syslog
from text2sound import play_sound, text2soundfile, AUDIO_DIR

FILENAME_PATTERN = AUDIO_DIR + '{}/insult{}.aiff'

class Insulter:

    def __init__(self):
        syslog.openlog('insultr', 0, syslog.LOG_LOCAL4)
        with open(os.path.dirname(os.path.abspath(__file__)) + '/insult_db.json') as json_data:
            self.ins_data = json.load(json_data)
            json_data.close()
            #pprint(d)

    def pickRandom(self, list):
        idx = random.randint(0, len(list) - 1)
        return list[idx], idx 


    def pickAdjektiv(self, g, idx):
        arr = self.ins_data['adjektive']
        rnd = random.randint(0, len(arr) - 1)
        return arr[rnd][g]


    def pickSubstantiv(self, idx):
        arr = self.ins_data['substantive']
        if idx < 0:
            rnd = random.randint(0, len(arr) - 1)
        return (arr[rnd]['wert'], arr[rnd]['geschlecht'])


    def pickSteigerung(self, g, idx):
        arr = self.ins_data['steigerungen']
        rnd = random.randint(0, len(arr) - 1)
        return arr[rnd]


    def get_insult(self, idx_steig, idx_adj, idx_sub):
        subst, g = self.pickSubstantiv(idx_sub)
        return "Du " + self.pickSteigerung(g, idx_steig) + " " + self.pickAdjektiv(g, idx_adj) + " " + subst


    def speak_next_insult(self, ziel_geschlecht, control=0, speed=0):

        #max = len(ins_data['steigerungen']) * len(ins_data['adjektive']) * len(ins_data['substantive'])
        max = 0
        if ziel_geschlecht == 'm':
            max = 2304
        else:
            max = 1344
        fn = FILENAME_PATTERN.format(ziel_geschlecht, random.randint(0, max))
        self.log("speaking insult " + str(fn))
        play_sound(fn, control*4, 1+((speed)/200.0))


    def create_insult_audio_db(self):
        male_count = 0
        female_count = 0
        for steig in self.ins_data['steigerungen']:
            for adj in self.ins_data['adjektive']:
                for subs in self.ins_data['substantive']:
                    g = subs['geschlecht']
                    substantiv = subs['wert']
                    ziel = subs['ziel'] # zielgeschlecht - f oder m
                    if ziel == "m":
                        male_count += 1
                        filename = FILENAME_PATTERN.format(ziel, male_count)
                    else: 
                        female_count += 1
                        filename = FILENAME_PATTERN.format(ziel, female_count)

                    adjektiv = adj[g]
                    steigerung = steig
                    text = "Du {} {} {}".format(steigerung, adjektiv, substantiv)
                    #log "Writing {} to {}".format(text, filename)
                    text2soundfile(text, filename)

    def log(self, msg):
        syslog.syslog(msg)

if __name__ == "__main__":
    insulter = Insulter()
    #create_insult_audio_db()

    insult = insulter.get_insult(-1, -1, -1)
    print insult
    insulter.speak_next_insult("m")

