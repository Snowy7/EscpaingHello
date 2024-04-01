import math
import pygame
from entities.Spritesheet import SpriteSheet
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__ (self, pos, groups, obstacle_sprites, interactable_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('./assets/images/hero_basic.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
        self.interactable_sprites = interactable_sprites
        
        self.lastInteracted = None
        self.didPressE = False
        self.lookDir = 0
        self.order = 10
        
        self.canMove = True
        
        self.glow_radius = 3

    def input(self):
        if not self.canMove:
            self.direction = pygame.math.Vector2(0, 0)
            return
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        
        # inverse image if moving left
        if self.direction.x < 0 and self.lookDir == 0:
            self.image = pygame.transform.flip(self.image, True, False)
           
            self.lookDir = 1
        elif self.direction.x > 0 and self.lookDir == 1:                
                self.image = pygame.transform.flip(self.image, True, False)
                self.lookDir = 0
         # remove black background
        self.image.set_colorkey((0, 0, 0))
        self.Interact()

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.canCollide and sprite.hitbox.colliderect(self.hitbox):
                    # check if is a PushableSprite
                    if hasattr(sprite, 'move'):
                        # get the dir between the player and the sprite
                        # check if player is moving towards the sprite
                        dir = pygame.math.Vector2(sprite.hitbox.center) - pygame.math.Vector2(self.hitbox.center)
                        dir = dir.normalize()

                        if dir.dot(self.direction) > 0.2: 
                            sprite.move(self.direction, self.speed)
                            continue
                    else:     
                        if self.direction.x > 0:  # moving right
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0:  # moving left
                            self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.canCollide and sprite.hitbox.colliderect(self.hitbox):
                    if hasattr(sprite, 'move'):
                        dir = pygame.math.Vector2(sprite.hitbox.center) - pygame.math.Vector2(self.hitbox.center)
                        dir = dir.normalize()
                        if dir.dot(self.direction) > 0.2:
                            sprite.move(self.direction, self.speed)
                            continue
                    else:
                        if self.direction.y > 0:  # moving down
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0:  # moving up
                            self.hitbox.top = sprite.hitbox.bottom

    def Interact(self):
        isInteracting = False
        targetSprite = None
        for sprite in self.interactable_sprites:
            if sprite.interactBox.colliderect(self.hitbox) and sprite.canInteract:
                isInteracting = True
                targetSprite = sprite
                break
            
        if isInteracting:
            # Draw "Press E to interact" on the screen
            wind = pygame.display.get_surface()
            font = pygame.font.Font(None, 36)
            msg = targetSprite.msg if hasattr(targetSprite, 'msg') else "Press E to interact"
            text = font.render(msg, True, 'white')
            wind.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 100))
            # Check if E is down only once NOT HOLDING
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                if not self.didPressE:
                    targetSprite.interact()
                    self.lastInteracted = targetSprite
                    self.didPressE = True
            else:
                self.didPressE = False
            
    def update(self):
        self.input()
        self.move(self.speed)
         
    def generate_glow(self, color, glow):
        radius = self.glow_radius * TILESIZE
        surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        
        layers = 25
        
        # get the starting opacity from the glow max is 255
        startingOpacity = glow
        
        for i in range(layers):
            opacity = startingOpacity - ((1 - i / layers) * startingOpacity)
            
            pygame.draw.circle(surf, (color[0], color[1], color[2], opacity), surf.get_rect().center, radius - i * 3)
            
        return surf
    
    def get_glow_radius(self): return self.glow_radius
    
    def clamp(self, n, smallest, largest): return max(smallest, min(n, largest))
    
    def change_to_knight(self):
        self.anim_wake = SpriteSheet(pygame.image.load("./assets/player/wake.png"))
        self.idle = self.anim_wake.get_image(4, (8, 0), (30, 26), 2)
        
        self.image = self.idle
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        
        # remove black background
        self.image.set_colorkey((0, 0, 0))