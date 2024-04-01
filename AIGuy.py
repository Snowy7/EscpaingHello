import random
import pygame
from settings import *

ghostSounds = [
    "v1.mp3",
    "v2.mp3",
    "v3.mp3",
    "v4.mp3",
    "v5.mp3",
    "v6.mp3",
    "v7.mp3",
    "v8.mp3",
    "v9.mp3",
    "v10.mp3",
]

class Ghost:
    def __init__(self, audio_manager) -> None:
        self.sounds = [pygame.mixer.Sound(f"./assets/audio/ghost/{sound}") for sound in ghostSounds]
        self.currentSound = None
        self.volume = 0.5
        
        self.delay = 15000
        self.lastPlayed = -self.delay
        
        self.played_sounds = []
        
        self.audio_manager = audio_manager
        self.hasNext = False
        
    def play(self):
        if not self.hasNext:
            if len(self.played_sounds) == len(self.sounds):
                self.played_sounds = []

            sounds = [sound for sound in self.sounds if sound not in self.played_sounds]            
            self.currentSound = random.choice(sounds)
            self.played_sounds.append(self.currentSound)
        else:
            self.currentSound = self.hasNext
            self.hasNext = False
            
        self.lastPlayed = pygame.time.get_ticks()
        self.audio_manager.queue(self.currentSound, False)
        
    def PlayNext(self, sound):
        self.hasNext = sound
        self.play()
            
    def update(self, ticks):
        if ticks - self.lastPlayed > self.delay:
            self.play()