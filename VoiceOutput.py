import pyttsx3
#function to output the passed text
def speech(text):
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()