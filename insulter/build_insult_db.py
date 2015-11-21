from insulter import Insulter

if __name__ == "__main__":
    insulter = Insulter()
    insulter.create_insult_audio_db()

    insulter.speak_next_insult("m")
    insulter.speak_next_insult("f")