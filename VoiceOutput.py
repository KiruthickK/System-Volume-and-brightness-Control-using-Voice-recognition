import pyttsx3

def speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()