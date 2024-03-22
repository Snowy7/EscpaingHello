import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, image_path, pos, groups, layer = 2):
        super().__init__(groups)
        
        # scale 16x16 to 64x64
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        
        self._layer = layer

class Interactable(Tile):
    def __init__(self, image_path, pos, groups):
        super().__init__(image_path, pos, groups)
    
    def interact(self):
        print("Interacted")
    
class Ground(Tile):
    def __init__(self, pos, groups):
        super().__init__("./assets/images/floor_plain.png", pos, groups, 1)

class Wall2(Tile):
    def __init__(self, pos, groups):
        sprites = [
            "Wall_missing_brick_1",
            "Wall_missing_brick_2",
            "Wall_gratings",
            "Wall_pipe_1",
            "Wall_pipe_2",
            "Wall_goo"
        ]
        
        wallSprite = sprites[pygame.time.get_ticks() % len(sprites)]
        
        super().__init__("./assets/images/" + wallSprite + ".png", pos, groups)

class Wall():
    # a wall has three parts: start middle end
    def __init__(self, pos, groups):
        # draw three parts of the wall
        center = Tile("./assets/images/wall_center.png", pos, groups)
        top = Tile("./assets/images/Wall_top_center.png", (pos[0], pos[1] - TILESIZE), groups)

class TestInteractable(Interactable):
    def __init__(self, pos, groups):
        super().__init__("./assets/images/skull.png", pos, groups)
        