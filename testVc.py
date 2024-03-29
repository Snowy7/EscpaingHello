import pyttsx3
import threading

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')

def say(text):
    engine.say(text)
    engine.runAndWait()


speaker = threading.Thread(target=say, args=("Hello World",))
speaker.start()