import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, image_path, pos, groups, layer = 2, size = (TILESIZE, TILESIZE)):
        super().__init__(groups)
        
        # load the image, convert to alpha
        self.image = pygame.image.load(image_path).convert_alpha()
        # scale the image to the tilesize defined in settings
        self.image = pygame.transform.scale(self.image, size)
        # get the rectangle of the image and set the topleft to the pos
        self.rect = self.image.get_rect(topleft = pos)
        
        self.hitbox = self.rect.inflate(0, -10)
        
        self.order = layer

        self.canCollide = True

class TileInteractable(Tile):
    def __init__(self, image_path, pos, groups):
        super().__init__(image_path, pos, groups)
        self.canInteract = True

        self.interactBox = self.hitbox.inflate(40, 40)

    def interact(self):
        print("Interacted")
    
class Ground(Tile):
    def __init__(self, pos, groups):
        super().__init__("./assets/images/floor_plain.png", pos, groups, layer = 1)

class Box(Tile):
    def __init__(self, pos, groups):
        super().__init__("./assets/images/boxes_stacked.png", pos, groups, layer = 1)        

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
        stain_images = [
            "./assets/images/floor_stain_1.png",
            "./assets/images/floor_stain_2.png",
            "./assets/images/floor_stain_3.png"
        ]
        center = Tile("./assets/images/wall_center.png", pos, groups)
        top = Tile("./assets/images/Wall_top_center.png", (pos[0], pos[1] - TILESIZE), [groups[0]])
       # stain = Tile(stain_images[pygame.time.get_ticks() % len(stain_images)], (pos[0], pos[1] + TILESIZE), [groups[0]])
    
class BottomWall():
    def __init__(self,pos,groups):
        top = Tile("./assets/images/Wall_top_center.png", (pos[0], pos[1]), groups)
        top.image = pygame.transform.rotate(top.image, 180)

class TopWall():
    def __init__(self,pos,groups):
        top = Tile("./assets/images/Wall_top_center.png", (pos[0], pos[1]), groups)        
        

class LeftWall():
    # a wall has three parts: start middle end
    def __init__(self, pos, groups):
        # draw three parts of the wall
        center = Tile("./assets/images/Wall_outer_w2.png", pos, groups)
        # make it so it is 10px on width
        center.hitbox = center.rect.inflate(-TILESIZE + 10, 0)
        # move the hitbox to the right
        center.hitbox.move_ip(10, 0)
    
class RightWall():
    # a wall has three parts: start middle end
    def __init__(self, pos, groups):
        # draw three parts of the wall
        center = Tile("./assets/images/Wall_outer_e2.png", pos, groups)
        # make it so it is 10px on width
        center.hitbox = center.rect.inflate(-TILESIZE + 10, 0)
        # move the hitbox to the left
        center.hitbox.move_ip(-10, 0)

class BottomLeft():
    def __init__(self, pos, groups):
        # draw three parts of the wall
        center = Tile("./assets/images/Wall_outer_sw.png", pos, groups)
        center.hitbox = center.rect.inflate(-TILESIZE + 10, 0)
        # move the hitbox to the left
        center.hitbox.move_ip(10, 0)

class BottomRightCorner():
    def __init__(self, pos, groups):
        # draw three parts of the wall
        center = Tile("./assets/images/Wall_inner_se.png", pos, groups)
        center.hitbox = center.rect.inflate(-TILESIZE + 10, 0)
        # move the hitbox to the left
        center.hitbox.move_ip(10, 0)
        
class TopRightCorner():
    def __init__(self, pos, groups):
        center = Tile("./assets/images/Wall_inner_sw.png", pos, groups)
        center.image = pygame.transform.rotate(center.image, 180)
        center.hitbox = center.rect.inflate(-TILESIZE + 10, 0)
        center.hitbox.move_ip(10, 0)
        
class TopLeftCorner():
    def __init__(self, pos, groups):
        center = Tile("./assets/images/Wall_inner_se.png", pos, groups)
        center.image = pygame.transform.rotate(center.image, 180)
        center.hitbox = center.rect.inflate(-TILESIZE + 10, 0)
        center.hitbox.move_ip(10, 0)

class BottomLeftCorner():
    def __init__(self, pos, groups):
        center = Tile("./assets/images/Wall_inner_sw.png", pos, groups)
        center.hitbox = center.rect.inflate(-TILESIZE + 10, 0)
        center.hitbox.move_ip(10, 0)
        


class BottomRight():
    def __init__(self, pos, groups):
        # draw three parts of the wall
        center = Tile("./assets/images/Wall_outer_se.png", pos, groups)
        center.hitbox = center.rect.inflate(-TILESIZE + 10, 0)
        # move the hitbox to the left
        center.hitbox.move_ip(-10, 0)

class TopLeft():
    def __init__(self, pos, groups):
        # draw three parts of the wall
        center = Tile("./assets/images/Wall_outer_w2.png", pos, groups)
        center.hitbox = center.rect.inflate(-TILESIZE + 10, 0)
        # move the hitbox to the left
        center.hitbox.move_ip(10, 0)
        top = Tile("./assets/images/Wall_outer_nw.png", (pos[0], pos[1] - TILESIZE), [groups[0]])

class TopRight():
    def __init__(self, pos, groups):
        # draw three parts of the wall
        center = Tile("./assets/images/Wall_outer_e2.png", pos, groups)
        center.hitbox = center.rect.inflate(-TILESIZE + 10, 0)
        # move the hitbox to the left
        center.hitbox.move_ip(-10, 0)
        top = Tile("./assets/images/Wall_outer_ne.png", (pos[0], pos[1] - TILESIZE), [groups[0]])
    

class TestInteractable(TileInteractable):
    def __init__(self, pos, groups):
        super().__init__("./assets/images/skull.png", pos, groups)

class BaseChest(TileInteractable):
    def __init__(self, pos, groups, closed_img, opened_img):
        super().__init__(closed_img, pos, groups)
        self.opened_img = opened_img
        
    def interact(self):
        print("Chest opened")
        self.image = pygame.image.load(self.opened_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
        self.hitbox = self.rect.inflate(0, -10)
        
        self.canInteract = False

class BaseDoor(TileInteractable):
    def __init__(self, pos, groups, closed_img, opened_img):
        super().__init__(closed_img, pos, groups)
        self.opened_img = opened_img
        self.closed_img = closed_img

        self.image = pygame.transform.scale(self.image, size=(TILESIZE*2.5, TILESIZE*2))
        self.rect.topleft = (pos[0] - TILESIZE/1.3, pos[1] - TILESIZE)
        
        self.pos = pos

        self.order = 20
        
    def interact(self):
        print("Gate Opened")
        self.image = pygame.image.load(self.opened_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.image = pygame.transform.scale(self.image, size=(TILESIZE*2.5, TILESIZE*2))
        self.rect = self.image.get_rect(topleft = (self.pos[0] - TILESIZE/1.3, self.pos[1] - TILESIZE))
        
        self.canInteract = False    
        self.canCollide = False    


class Door(BaseDoor):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, "./assets/images/door_closed.png", "./assets/images/door_open.png")

class Chest(BaseChest):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, "./assets/images/chest_closed.png", "./assets/images/chest_open_empty.png")

class GoldenChest(BaseChest):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, "./assets/images/chest_golden_closed.png", "./assets/images/chest_golden_open_full.png")

        