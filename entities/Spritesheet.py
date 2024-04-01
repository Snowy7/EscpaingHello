import pygame
from settings import *


class SpriteSheet():
	def __init__(self, image):
		self.sheet = image
		self.sheet.set_colorkey((0, 0, 0))

	def get_image(self, frame, offset, w_h, scale, colorkey = (0, 0, 0)):
		image = pygame.Surface(w_h).convert_alpha()
		image.blit(self.sheet, (0, 0), (0 + offset[0], (frame * w_h[1]) + offset[1], w_h[0], w_h[1]))
		image = pygame.transform.scale(image, (w_h[0] * scale, w_h[1] * scale))
		image.set_colorkey(colorkey)
		return image

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, path, offset, w_h, scale, framesCount):
        super().__init__()
        
        self.anim = SpriteSheet(pygame.image.load(path))
        self.frames = [
            self.anim.get_image(i, offset, w_h, scale) for i in range(framesCount)
        ]
        self.image = self.frames[0]
        self.current_frame = 0
        self.last_update = 0
        self.frame_rate = FPS
    
    def animate(self, dir):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            
            if dir == 0:
                self.image = pygame.transform.flip(self.image, True, False)

        
         