#!/usr/bin/python
# insulter.py

import os
import json
import random
import syslog
from text2sound import play_sound, text2soundfile

MY_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DB_DIR = os.getenv('AUDIO_DB_DIR', MY_DIR + "/audio_db")
AUDIO_DB_FILE = AUDIO_DB_DIR + "/insult_db.json"
AUDIO_DB_FILE_INDEX_ZIELGESCHLECHT = AUDIO_DB_DIR + "/insult_db_index_zielgeschlecht.json"
FILENAME_PATTERN = '/insult{}.aiff'

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
        play_sound(AUDIO_DB_DIR + insult['filename'], control*4, 1+((speed)/200.0))


    def create_insult_audio_db(self):
        with open(MY_DIR + '/insult_db.source.json') as json_data:
            insult_db_source = json.load(json_data)
            json_data.close()
            #pprint(d)

        if not os.path.isdir(AUDIO_DB_DIR):
            os.makedirs(AUDIO_DB_DIR)

        insult_db = {}
        insult_db_index_zielgeschlecht = {}
        insult_db_index_zielgeschlecht['m'] = []
        insult_db_index_zielgeschlecht['f'] = []

        #female = True
        count = 0
        male_count = 0
        female_count = 0
        for steig in insult_db_source['steigerungen']:
            for adj in insult_db_source['adjektive']:
                for subst in insult_db_source['substantive']:

                    grammatik_geschlecht = subst['geschlecht']
                    substantiv = subst['wert']
                    zielgeschlecht = subst['ziel'] # zielgeschlecht - f oder m
                    adjektiv = adj[grammatik_geschlecht]
                    steigerung = steig

                    text = "Du {} {} {}".format(steigerung, adjektiv, substantiv)
                    filename = FILENAME_PATTERN.format(count)
                    
                    if zielgeschlecht == "m":
                        male_count += 1
                        female = False
                        insult_db_index_zielgeschlecht['m'].append(count)
                    else: 
                        female_count += 1
                        female = True
                        insult_db_index_zielgeschlecht['f'].append(count)
                    
                    print "female_count:{}, male_count:{}, female:{}".format(female_count, male_count, female)
                    
                    insult_db[count] = { 
                        'steigerung': steigerung, 
                        'adjektiv': adjektiv,
                        'substantiv': substantiv,
                        'zielgeschlecht': zielgeschlecht,
                        'filename': filename,
                        'text': text
                    }

                    #text2soundfile(text, filename, overwrite=True, female=female)
                    #print json.dumps(insult_db, indent=4)
                    count += 1

        insult_db['female_count'] = female_count
        insult_db['male_count'] = male_count

        out_file = open(AUDIO_DB_FILE,"w")
        json.dump(insult_db, out_file, indent=4)    
        out_file.close()

        out_file = open(AUDIO_DB_FILE_INDEX_ZIELGESCHLECHT,"w")
        json.dump(insult_db_index_zielgeschlecht, out_file, indent=4)    
        out_file.close()

    def say_hello(self):
        play_sound(AUDIO_DB_DIR + "/hello.aiff")

    def log(self, msg):
        print msg
        syslog.syslog(msg)

if __name__ == "__main__":
    insulter = Insulter()
    #insulter.create_insult_audio_db()

    insulter.speak_next_insult("m")
    insulter.speak_next_insult("f")

