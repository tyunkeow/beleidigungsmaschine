#!/usr/bin/python
# insulter.py

import json
import random
from text2sound import play_sound, text2soundfile, AUDIO_DIR


ins_data = {
    "adjektive": [
        {
            'm': "haesslicher",
            "f": "haessliche",
            "n": "haessliches"
        },
        {
            "m": "buckliger",
            "f": "bucklige",
            "n": "buckliges"
        },
        {
            "m": "besoffener",
            "f": "besoffene",
            "n": "besoffenes"
        },
        {
            "m": "fieser",
            "f": "fiese",
            "n": "fieses"
        },
        {
            "m": "tollpatschiger",
            "f": "tollpatschige",
            "n": "tollpatschiges"
        },
        {
            "m": "grosser",
            "f": "grosse",
            "n": "grosses"
        },
        {
            "m": "unverschaemter",
            "f": "unverschaemte",
            "n": "unverschaemtes"
        },
        {
            "m": "vorlauter",
            "f": "vorlaute",
            "n": "vorlautes"
        },
        {
            "m": "brutaler",
            "f": "brutale",
            "n": "brutales"
        },
        {
            "m": "schlechter",
            "f": "schlechte",
            "n": "schlechtes"
        },
        {
            "m": "gewissenloser",
            "f": "gewissenlose",
            "n": "gewissenloses"
        },
        {
            "m": "ruecksichtsloser",
            "f": "ruecksichtslose",
            "n": "ruecksichtsloses"
        },
        {
            "m": "bemitleidenswerter",
            "f": "bemitleidenswerte",
            "n": "bemitleidenswertes"
        },
        {
            "m": "haariger",
            "f": "haarige",
            "n": "haariges"
        },
        {
            "m": "verstrahlter",
            "f": "verstrahlte",
            "n": "verstrahltes"
        },
        {
            "m": "kleiner",
            "f": "kleine",
            "n": "kleines"
        }
    ],
    "steigerungen": ["sehr", "massiv", "extrem", "besonders", "ausserordentlich", "super"],
    "substantive": [
        {
            "geschlecht": "m",
            "wert": "Affe",
            "ziel": "m"
        },
        {
            "geschlecht": "f",
            "wert": "Geissel der Menschheit",
            "ziel": "m"
        },
        {
            "geschlecht": "f",
            "wert": "Geissel der Menschheit",
            "ziel": "f"
        },
        {
            "geschlecht": "m",
            "wert": "Fuerst der Finsternis",
            "ziel": "m"
        },
        {
            "geschlecht": "f",
            "wert": "Fuerstin der Finsternis",
            "ziel": "f"
        },
        {
            "geschlecht": "n",
            "wert": "Stinktier",
            "ziel": "m"
        },
        {
            "geschlecht": "m",
            "wert": "Heckenpenner",
            "ziel": "m"
        },
        {
            "geschlecht": "m",
            "wert": "Schweinepriester",
            "ziel": "m"
        },
        {
            "geschlecht": "f",
            "wert": "Schweinepriesterin",
            "ziel": "f"
        },
        {
            "geschlecht": "m",
            "wert": "Luegenbaron",
            "ziel": "m"
        },
        {
            "geschlecht": "m",
            "wert": "Doedel",
            "ziel": "m"
        },
        {
            "geschlecht": "m",
            "wert": "Erbsenzaehler",
            "ziel": "m"
        },
        {
            "geschlecht": "m",
            "wert": "Ruepel",
            "ziel": "m"
        },
        {
            "geschlecht": "m",
            "wert": "Idiot",
            "ziel": "m"
        },
        {
            "geschlecht": "m",
            "wert": "Trottel",
            "ziel": "m"
        },
        {
            "geschlecht": "m",
            "wert": "Grotten-olm",
            "ziel": "m"
        },
        {
            "geschlecht": "m",
            "wert": "Pimmelbaer",
            "ziel": "m"
        },
        {
            "geschlecht": "n",
            "wert": "Schwein",
            "ziel": "m"
        },
        {
            "geschlecht": "n",
            "wert": "Froschgesicht",
            "ziel": "m"
        },
        {
            "geschlecht": "n",
            "wert": "Froschgesicht",
            "ziel": "f"
        },
        {
            "geschlecht": "n",
            "wert": "Pupsgesicht",
            "ziel": "m"
        },
        {
            "geschlecht": "n",
            "wert": "Huhn",
            "ziel": "f"
        },
        {
            "geschlecht": "n",
            "wert": "Luder",
            "ziel": "f"
        },
        {
            "geschlecht": "n",
            "wert": "Horrt-kind",
            "ziel": "m"
        },
        {
            "geschlecht": "n",
            "wert": "Horrt-kind",
            "ziel": "f"
        },
        {
            "geschlecht": "f",
            "wert": "Hexe",
            "ziel": "f"
        },
        {
            "geschlecht": "f",
            "wert": "Made",
            "ziel": "m"
        },
        {
            "geschlecht": "f",
            "wert": "Made",
            "ziel": "f"
        },
        {
            "geschlecht": "f",
            "wert": "Schlampe",
            "ziel": "f"
        },
        {
            "geschlecht": "f",
            "wert": "Hackfresse",
            "ziel": "m"
        },
        {
            "geschlecht": "m",
            "wert": "Sesselfurzer",
            "ziel": "m"
        },
        {
            "geschlecht": "f",
            "wert": "Sesselfurzerin",
            "ziel": "f"
        },
        {
            "geschlecht": "f",
            "wert": "Sau",
            "ziel": "f"
        },
        {
            "geschlecht": "f",
            "wert": "Kartoffelnase",
            "ziel": "m"
        },
        {
            "geschlecht": "f",
            "wert": "Flachzange",
            "ziel": "m"
        },
        {
            "geschlecht": "f",
            "wert": "Evolutionsbremse",
            "ziel": "m"
        },
        {
            "geschlecht": "f",
            "wert": "Evolutionsbremse",
            "ziel": "f"
        },
        {
            "geschlecht": "f",
            "wert": "Dumpfbacke",
            "ziel": "f"
        }
    ]
}


FILENAME_PATTERN = AUDIO_DIR + '{}/insult{}.aiff'


def pickRandom(list):
    return 0


def pickAdjektiv(g, idx):
    arr = ins_data['adjektive']
    rnd = random.randint(0, len(arr) - 1)
    return arr[rnd][g]


def pickSubstantiv(idx):
    arr = ins_data['substantive']
    if idx < 0:
        rnd = random.randint(0, len(arr) - 1)
    return (arr[rnd]['wert'], arr[rnd]['geschlecht'])


def pickSteigerung(g, idx):
    arr = ins_data['steigerungen']
    rnd = random.randint(0, len(arr) - 1)
    return arr[rnd]


def get_insult(idx_steig, idx_adj, idx_sub):
    subst, g = pickSubstantiv(idx_sub)
    return "Du " + pickSteigerung(g, idx_steig) + " " + pickAdjektiv(g, idx_adj) + " " + subst


def speak_next_insult(ziel_geschlecht, control=0, speed=0):

    #max = len(ins_data['steigerungen']) * len(ins_data['adjektive']) * len(ins_data['substantive'])
    max = 0
    if ziel_geschlecht == 'm':
        max = 2304
    else:
        max = 1344
    fn = FILENAME_PATTERN.format(ziel_geschlecht, random.randint(0, max))
    print "speaking insult " + str(fn)
    play_sound(fn, control*4, 1+((speed)/200.0))


def create_insult_audio_db():
    male_count = 0
    female_count = 0
    for steig in ins_data['steigerungen']:
        for adj in ins_data['adjektive']:
            for subs in ins_data['substantive']:
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
                #print "Writing {} to {}".format(text, filename)
                text2soundfile(text, filename)


if __name__ == "__main__":
    #create_insult_audio_db()

    insult = get_insult(-1, -1, -1)
    print insult
    speak_next_insult("m")

