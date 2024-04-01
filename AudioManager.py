import pygame
from settings import *

class AudioManager:
    def __init__(self):
        self._vfx_audio = None
        self._ghost_audio = None
        
        pygame.mixer.init()
        pygame.mixer.set_num_channels(2)
        
        self._vfx_channel = pygame.mixer.Channel(0)
        self._vfx_channel.set_volume(VFX_VOLUME)
        self._ghost_channel = pygame.mixer.Channel(1)
        self._ghost_channel.set_volume(GHOST_VOLUME)
        
        # Queue up the sounds
        self._vfx_queue = []
        self._ghost_queue = []
    
    def queue(self, sound, isVFX = True):
        if isVFX:
            self._vfx_queue.append(sound)
        else:
            print("Queueing ghost sound")
            self._ghost_queue.append(sound)
     
    def play(self, sound, isVFX = True):
        if isVFX:
            self._vfx_audio = sound
            self._vfx_channel.play(sound)
        else:
            self._ghost_audio = sound
            self._ghost_channel.play(sound)
    
    def isVFXPlaying(self):
        return self._vfx_audio is not None
    
    def fadeout(self, isVFX = True):
        if isVFX:
            self._vfx_channel.fadeout(100)
        else:
            self._ghost_channel.fadeout(100)
    
    def update(self):
        if not self._vfx_channel.get_busy():
            self._vfx_audio = None
            if len(self._vfx_queue) > 0:
                self.play(self._vfx_queue.pop(0), True)
            
                    
        if not self._ghost_channel.get_busy():
            self._ghost_audio = None
            if len(self._ghost_queue) > 0:
                self.play(self._ghost_queue.pop(0), False)
        
    def stop(self):
        self._audio.stop()