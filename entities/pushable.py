import pygame

from entities.tiles import Tile

class PushableSprite(Tile):
    def __init__(self, pos, groups, obstacle_sprites, audio_manager):
        super().__init__("./assets/images/boxes_stacked.png", pos, groups)
        
        self.audio_manager = audio_manager
        self.box_slide = pygame.mixer.Sound('./assets/audio/WoodDrag.wav')
        self.obstacle_sprites = obstacle_sprites
        self.canCollide = True
        
        self.order = 2
        
        self.wasMoving = False
        self.moving = False
        self.canPush = True

    def move(self, direction, speed):
        if not self.canPush: return
        self.hitbox.x += direction.x * speed
        self.rect.center = self.hitbox.center
        self.collision('horizontal', direction)
        self.hitbox.y += direction.y * speed
        self.rect.center = self.hitbox.center
        self.collision('vertical', direction)
        self.rect.center = self.hitbox.center
        self.moving = True
    
    def update(self):
        if not self.canPush: return
        if self.moving:
            if not self.audio_manager.isVFXPlaying():
                self.audio_manager.queue(self.box_slide)
        elif self.wasMoving:
            self.audio_manager.fadeout()
            
        self.wasMoving = self.moving
        self.moving = False
        
    def collision(self, dr, direction = pygame.math.Vector2()):
       if dr == 'horizontal':
           for sprite in self.obstacle_sprites:
               if sprite == self: continue
               if sprite.canCollide and sprite.hitbox.colliderect(self.hitbox):
                   if direction.x > 0:  # moving right
                       self.hitbox.right = sprite.hitbox.left
                   if direction.x < 0:  # moving left
                       self.hitbox.left = sprite.hitbox.right

       if dr == 'vertical':
           for sprite in self.obstacle_sprites:
               if sprite == self: continue
               
               if sprite.canCollide and sprite.hitbox.colliderect(self.hitbox):
                    if direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom
       
class LetterPushable(PushableSprite):
    def __init__(self, pos, groups, obstacle_sprites, audio_manager, letter = "E"):
        super().__init__(pos, groups, obstacle_sprites, audio_manager)
        
        self.image = pygame.image.load(f"./assets/images/letter_{letter}.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        
        self.letter = letter
        
    def snap(self, target):
        self.hitbox.center = target.hitbox.center
        self.rect.center = self.hitbox.center
        self.canPush = False
        
        self.audio_manager.fadeout()