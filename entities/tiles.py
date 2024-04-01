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

class Animated(pygame.sprite.Sprite):
    def __init__(self, images, pos, groups, layer = 2):
        super().__init__(groups)
        
        self.images = images
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.current_frame = 0
        self.last_update = 0
        self.frame_rate = FPS
        
        self.order = layer
        self.canCollide = False
        
        
    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.image = self.images[self.current_frame]
            self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))

class Tourch(Animated):
    def __init__(self, pos, groups, layer = 2, isFlame = True, radius = 3):
        images = [pygame.image.load("./assets/images/torch_{0}.png".format(i)).convert_alpha() for i in range(1, 8)]
        self.no_flame = pygame.image.load("./assets/images/torch_no_flame.png").convert_alpha()
        
        self.no_flame = pygame.transform.scale(self.no_flame, (TILESIZE, TILESIZE))
        self.isFlame = isFlame
        self.radius = radius
        
        super().__init__(images, pos, groups, layer=layer)
        
        self.frame_rate = FPS * 2
        
    def turn_off(self):
        self.isFlame = False
        
    def turn_on(self):
        self.isFlame = True
        
    def update(self):
        if self.isFlame:
            self.animate()
        else:
            self.image = self.no_flame
            
    def generate_glow(self, color, glow):
        radius = self.radius * TILESIZE
        surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        
        layers = 25
        
        # get the starting opacity from the glow max is 255
        startingOpacity = glow
        
        for i in range(layers):
            opacity = startingOpacity - ((1 - i / layers) * startingOpacity)
            
            pygame.draw.circle(surf, (color[0], color[1], color[2], opacity), surf.get_rect().center, radius - i * 3)
            
        return surf
    
    def get_radius(self): return self.radius
    
    
    def clamp(self, n, smallest, largest): return max(smallest, min(n, largest))

class TileInteractable(Tile):
    def __init__(self, image_path, pos, groups):
        super().__init__(image_path, pos, groups)
        self.canInteract = True

        self.interactBox = self.hitbox.inflate(40, 40)
        
        self.msg = "Press E to interact"

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

class SpecialWall():
    # a wall has three parts: start middle end
    def __init__(self, pos, groups, audio_manager):
        # draw three parts of the wall
        stain_images = [
            "./assets/images/floor_stain_1.png",
            "./assets/images/floor_stain_2.png",
            "./assets/images/floor_stain_3.png"
        ]
        self.center = Tile("./assets/images/wall_center.png", pos, groups)
        self.top = Tile("./assets/images/Wall_top_center.png", (pos[0], pos[1] - TILESIZE), [groups[0]])
       # stain = Tile(stain_images[pygame.time.get_ticks() % len(stain_images)], (pos[0], pos[1] + TILESIZE), [groups[0]])

        self.breakSound = pygame.mixer.Sound("./assets/audio/BricksHit.wav")
        self.audio_manager = audio_manager
    def kill(self):
        self.center.kill()
        self.top.kill()
        self.audio_manager.play(self.breakSound, True)
    
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
    def __init__(self, pos, groups, level):
        super().__init__("./assets/images/skull.png", pos, groups)
        self.level = level
        
    def interact(self):
        for sw in self.level.specialWalls:
            sw.kill()

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
    def __init__(self, pos, groups, closed_img, opened_img, canBeInteracted = False, audio_manager = None):
        super().__init__(closed_img, pos, groups)
        self.opened_img = opened_img
        self.closed_img = closed_img

        self.image = pygame.transform.scale(self.image, size=(TILESIZE*2.5, TILESIZE*2))
        self.rect.topleft = (pos[0] - TILESIZE/1.3, pos[1] - TILESIZE)
        
        self.pos = pos
        self.canBeInteracted = canBeInteracted
        self.audio_manager = audio_manager
        
        self.open_sound = pygame.mixer.Sound("./assets/audio/Door Open.wav")
        self.close_sound = pygame.mixer.Sound("./assets/audio/Door Close.wav")

        self.order = 20
        
    def interact(self):
        # You are not allowed to open the door
        pass 
    
    def Open(self):
        self.image = pygame.image.load(self.opened_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.image = pygame.transform.scale(self.image, size=(TILESIZE*2.5, TILESIZE*2))
        self.rect = self.image.get_rect(topleft = (self.pos[0] - TILESIZE/1.3, self.pos[1] - TILESIZE))
        
        self.canInteract = False    
        self.canCollide = False
        
        # play open sound
        if self.audio_manager is not None: self.audio_manager.queue(self.open_sound, True)
    
    def Close(self):
        self.image = pygame.image.load(self.closed_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.image = pygame.transform.scale(self.image, size=(TILESIZE*2.5, TILESIZE*2))
        self.rect = self.image.get_rect(topleft = (self.pos[0] - TILESIZE/1.3, self.pos[1] - TILESIZE))
        
        self.canInteract = True
        self.canCollide = True 
        
        if self.audio_manager is not None: self.audio_manager.queue(self.close_sound, True)

class Door(BaseDoor):
    def __init__(self, pos, groups, audio_manager):
        super().__init__(pos, groups, "./assets/images/door_closed.png", "./assets/images/door_open.png", audio_manager=audio_manager)
        self.msg = "You can't open this door like this!"

class FlippedDoor(Door):
    def __init__(self, pos, groups, audio_manager):
        super().__init__(pos, groups, audio_manager=audio_manager)
        # flip on the x axis
        self.rect.topleft = (self.rect.topleft[0], pos[1]  - TILESIZE/3.3)
        
class Chest(BaseChest):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, "./assets/images/chest_closed.png", "./assets/images/chest_open_empty.png")

class GoldenChest(BaseChest):
    def __init__(self, pos, groups, function = None):
        super().__init__(pos, groups, "./assets/images/chest_golden_closed.png", "./assets/images/chest_golden_open_full.png")
        self.func = function
    
    def interact(self):
        super().interact()
        print("You found a golden chest!")
        if self.func is not None:
            self.func()       

class PressurePlate(Tile):
    def __init__(self, pos, groups, obstacle_sprites, level):
        super().__init__("./assets/images/black.png", pos, groups)
        self.obstacle_sprites = obstacle_sprites
        self.level = level
        self.order = 1
        
        self.isActivated = False
        self.collidedWith = None
        
    def update(self):
        # check if any colliding with the pressure plate
        self.collision()
        pass
    
    def collision(self):
        isActivated = False
        for sprite in self.obstacle_sprites:
                if sprite.canCollide and sprite.hitbox.colliderect(self.hitbox):
                    isActivated = True
                    self.collidedWith = sprite
                    break
        
        if isActivated != self.isActivated:
            self.isActivated = isActivated
            self.activatePressurePlate(isActivated)
            
    
    def activatePressurePlate(self, isActivated):
        if isActivated:
            self.activate()
        else:
            self.deactivate()
                    
    
    def activate(self):
        # activate the pressure plate
        self.level.level_1_door.Open()
        pass
    
    def deactivate(self):
        # deactivate the pressure plate
        self.level.level_1_door.Close()
        pass
 
class Lave(TileInteractable):
    def __init__(self, pos, groups):
        super().__init__("./assets/images/lava.png", pos, groups)
        self.canInteract = True
        self.pos = pos
        self.groups = groups
        
        self.msg = "Oh Lava, I cannot go through this!"
        
    def interact(self):
        pass
    
    def turn_on(self):
        super().__init__("./assets/images/lava.png", self.pos, self.groups)
        self.msg = "Oh no, the lava is flowing!"
        self.canCollide = True
        
    def turn_off(self):
        super().__init__("./assets/images/black.png", self.pos, self.groups)
        self.msg = "Oh, the lava has solidified!"
        self.canCollide = False
 
class InteractableWall(TileInteractable):
    def __init__(self, pos, groups, function):
        super().__init__("./assets/images/wall_flag_red.png", pos, groups)
        self.func = function
        self.top = Tile("./assets/images/Wall_top_center.png", (pos[0], pos[1] - TILESIZE), [groups[0]])
        
        
    def interact(self):
        self.image = pygame.image.load("./assets/images/wall_flag_green.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.func()
        self.canInteract = False
        pass
    
class DLetter(Tile):
    def __init__(self, pos, groups):
        super().__init__("./assets/images/floor_D.png", pos, groups)
        self.canCollide = False
             
class LetterHolder(Tile):
    def __init__(self, pos, groups, obstacle_sprites, letter, level):
        super().__init__("./assets/images/black.png", pos, groups)
        self.obstacle_sprites = obstacle_sprites
        self.level = level
        self.letter = letter
        self.order = 1
        
        self.isActivated = False
        self.collidedWith = None
        
    def update(self):
        # check if any colliding with the pressure plate
        self.collision()
        pass
    
    def collision(self):
        isActivated = False
        for sprite in self.obstacle_sprites:
                if sprite.canCollide and sprite.hitbox.colliderect(self.hitbox):
                    # check if has a var called letter
                    if hasattr(sprite, "letter"):
                        if sprite.letter != self.letter:
                            # kill that sprite
                            sprite.kill()
                            self.level.removeHeart()
                            continue
                        sprite.snap(self)                       
                        isActivated = True
                        self.collidedWith = sprite
                        break
                    break
        
        if isActivated != self.isActivated:
            self.isActivated = isActivated
            #self.activatePressurePlate(isActivated)
            