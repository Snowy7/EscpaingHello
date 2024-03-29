import random
import pyttsx3
import threading


ANNOYING_STATEMENTS = [
    "You're not good at this game",
    "You're not even trying",
    "You're not even close",
    "Are you even trying?",
    "What are you even doing?",
    "Can you play seriously for once?",
    "My grandma plays better than you",
    "Even my dog plays better than you",
    "Even my cat plays better than you",
    "Even my goldfish plays better than you"
    "Even my racoon plays better than you",
]

class AIVoice:
    def __init__(self, index):
        self.engine = pyttsx3.init(driverName='sapi5')
        self.voices = self.engine.getProperty('voices')
        if index < len(self.voices):
            self.setVoice(index)
        else:
            self.setVoice(0)
                    
    def say(self, text):
        
        # stop the current speech
        self.engine.stop()
        
        self.engine.say(text)
        self.engine.runAndWait()
        
    def setVoice(self, index):
        if index < len(self.voices):
            self.engine.setProperty('voice', self.voices[index].id)
            
class AnnoyingAI(AIVoice):
    def __init__(self):
        super().__init__(1)
        self.saidText = []
        
        # Interval every 10 seconds
        self.interval = 10000
        self.last_run = 0
        
    def update(self, t):
        if t - self.last_run >= self.interval:
            self.last_run = t
            self.sayAnnoying()
        
        
        
    def sayAnnoyingAsync(self):
        text = ANNOYING_STATEMENTS[0]
        while text in self.saidText:
            text = ANNOYING_STATEMENTS[random.randint(0, len(ANNOYING_STATEMENTS) - 1)]
        self.saidText.append(text)
        if len(self.saidText) >= len(ANNOYING_STATEMENTS):
            self.saidText = []
            
        self.say(text)
        
        
            
    def sayAnnoying(self):
        speaker = threading.Thread(target=self.sayAnnoyingAsync)
        speaker.start()
    
        