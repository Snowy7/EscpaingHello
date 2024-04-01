import pygame
from AIGuy import Ghost
from AudioManager import AudioManager
from entities.pushable import LetterPushable, PushableSprite
from menu import MainMenu
from settings import *
from entities.tiles import DLetter, FlippedDoor, Ground, InteractableWall, Lave, LetterHolder, PressurePlate, SpecialWall, TopLeftCorner, TopRightCorner, Tourch, Wall, TestInteractable, Chest, GoldenChest, LeftWall,BottomLeft,TopLeft,BottomRight,TopRight,RightWall,BottomWall,TopWall,BottomRightCorner,BottomLeftCorner,Box,Door
from entities.player import Player

class Level3:
    def __init__(self, level):
        self.level = level
        self.maxHearts = 3
        self.hearts = self.maxHearts
        self.letterHolders = []
        self.isCompleted = False
        
        self.door = None
    
    def update(self):
        if self.isCompleted: return
        #render the hearts
        hearts = self.hearts
        for i in range(self.maxHearts):
            if i >= hearts:
                heart = pygame.image.load("./assets/images/heart_empty.png")
            else:
                heart = pygame.image.load("./assets/images/heart.png")
            heart = pygame.transform.scale(heart, (60, 60))
            self.level.display_surface.blit(heart, (20 + i * 30, 20))
        
        if self.checkCompleteion():
            print("Level 3 complete")
            if self.door:
                self.door.Open()
            self.isCompleted = True
    
    def removeHeart(self):
        self.hearts -= 1
        return self.hearts <= 0
    
    def checkCompleteion(self):
        for letterHolder in self.letterHolders:
            if not letterHolder.isActivated:
                return False
            
        return True   

class CheckPoint(pygame.sprite.Sprite):
    # takes the function to call when the checkpoint is reached
    def __init__(self, pos, groups, function, collisionGroup):
        super().__init__(groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill((0, 0, 0))
        # hide the checkpoint
        self.image.set_alpha(0)
        
        self.rect = self.image.get_rect(topleft = pos)
        self.order = 200
        
        self.hitbox = self.rect
        self.canCollide = False
        
        self.function = function
        self.collisionGroup = collisionGroup
        
    def update(self):
        self.collision()
        
    def collision(self):
        for sprite in self.collisionGroup:
            if sprite.hitbox.colliderect(self.hitbox):
                self.function()
                self.kill()
                break    
       
class Level:
    def __init__(self):
        # get the display surface 
        self.display_surface = pygame.display.get_surface()

        # sprite group set up
        self.visible_sprites = YSortCameraGroup()
        self.player_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.interactable_sprites = pygame.sprite.Group()
        self.background_sprites = pygame.sprite.Group()
        self.pressure_plate_sprites = pygame.sprite.Group()
        self.specialWalls = []
        self.tourches = []
        self.lave = []
        
        self.audio_manager = AudioManager()
        self.ghost = Ghost(self.audio_manager)
        
        self.level_1_door = None
        self.level_3_door = None
        
        self.level = 0
        self.level3 = Level3(self)
        
        self.finished = False
        self.mainMenu = MainMenu(self.start)

        # sprite set up
        self.create_map()
        self.done = False
        
        self.game_state = 0
        
    def start(self):
        self.game_state = 1

    def removeHeart(self):
        if self.level3.removeHeart():
            self.die()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                
                #Ground((x, y), [self.visible_sprites, self.background_sprites])
                if col == "ar":
                    continue 
                if col == 'wa':
                    Wall((x, y), [self.visible_sprites, self.obstacle_sprites])
                    continue
                if col == "lw":
                    LeftWall((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue
                if col == "rw":
                    RightWall((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue
                if col == "bl":
                    BottomLeft((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue                      
                if col == "br":
                    BottomRight((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue 
                if col == "tl":
                    TopLeft((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue 
                if col == "tr":
                    TopRight((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue 
                if col == "tw":
                    TopWall((x,y),[self.visible_sprites, self.obstacle_sprites])  
                    continue 
                if col == "bw":
                    BottomWall((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue 
                if col ==  "BRC":
                    BottomRightCorner((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue
                if col ==  "BLC":
                    BottomLeftCorner((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue
                if col ==  "TRC":
                    TopRightCorner((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue
                if col ==  "TLC":
                    TopLeftCorner((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue
                
                Ground((x, y), [self.visible_sprites, self.background_sprites])

                if col == 'swa':
                    self.specialWalls.append(SpecialWall((x, y), [self.visible_sprites, self.obstacle_sprites], self.audio_manager))
                    continue
                if col == "BL":
                    BottomLeft((x,y),[self.visible_sprites, self.obstacle_sprites])
                if col == "bx":
                    PushableSprite((x,y),[self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, self.audio_manager)               
                if col == "BR":
                    BottomRight((x,y),[self.visible_sprites, self.obstacle_sprites])       
                if col == "bw":
                    BottomWall((x,y),[self.visible_sprites, self.obstacle_sprites])
                if col == "LW":
                    LeftWall((x,y),[self.visible_sprites, self.obstacle_sprites])
                if col == "RW":
                    RightWall((x,y),[self.visible_sprites, self.obstacle_sprites])
                if col == "TL":
                    TopLeft((x,y),[self.visible_sprites, self.obstacle_sprites])    
                if col == "TR":
                    TopRight((x,y),[self.visible_sprites, self.obstacle_sprites])    
                if col == 'pl':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, self.interactable_sprites)
                    self.player_sprites.add(self.player)
                if col == "t":
                    TestInteractable((x, y), [self.visible_sprites, self.interactable_sprites])
                if col == "c":
                    Chest((x, y), [self.visible_sprites, self.interactable_sprites])
                if col == "dr1":
                    self.level_1_door = Door((x, y), [self.visible_sprites, self.obstacle_sprites, self.interactable_sprites], self.audio_manager) 
                if col == "dr3":
                    self.level_3_door = FlippedDoor((x, y), [self.visible_sprites, self.obstacle_sprites, self.interactable_sprites], self.audio_manager)
                    self.level3.door = self.level_3_door
                if col == "gc":
                    GoldenChest((x, y), [self.visible_sprites, self.interactable_sprites], self.change_player)                    
                if col == "sk":
                    TestInteractable((x, y), [self.visible_sprites, self.interactable_sprites], self)
                if col == "pp":
                    self.pressure_plate_sprites.add(PressurePlate((x, y), [self.visible_sprites, self.pressure_plate_sprites], self.obstacle_sprites, self))                
                if col == "t4":
                    self.tourches.append(Tourch((x, y), [self.visible_sprites, self.obstacle_sprites], isFlame=True, radius=4))
                if col == "t3":
                    self.tourches.append(Tourch((x, y), [self.visible_sprites, self.obstacle_sprites], isFlame=True, radius=3))              
                if col == "1p":
                    # first level checkpoint
                    CheckPoint((x, y), [self.visible_sprites], self.checkpoint_1, self.player_sprites)
                if col == "2p":
                    # second level checkpoint
                    CheckPoint((x, y), [self.visible_sprites], self.checkpoint_2, self.player_sprites)
                if col == "3p":
                    # third level checkpoint
                    CheckPoint((x, y), [self.visible_sprites], self.checkpoint_3, self.player_sprites)
                if col == "4p":
                    # fourth level checkpoint
                    CheckPoint((x, y), [self.visible_sprites], self.finish, self.player_sprites)                
                if col == "iw":
                    InteractableWall((x, y), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites], self.turn_off_lava)                 
                if col == "lv":
                    self.lave.append(Lave((x, y), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites]))
                if col == "dl":
                    DLetter((x, y), [self.visible_sprites])
                    
                if col == "lh-e":
                    self.level3.letterHolders.append(LetterHolder((x, y), [self.visible_sprites, self.pressure_plate_sprites], self.obstacle_sprites, "E", self))
                if col == "lh-a":
                    self.level3.letterHolders.append(LetterHolder((x, y), [self.visible_sprites, self.pressure_plate_sprites], self.obstacle_sprites, "A", self))
                if col == "la":
                    LetterPushable((x, y), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, self.audio_manager, "A")
                if col == "le":
                    LetterPushable((x, y), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, self.audio_manager)
                if col == "lo":
                    LetterPushable((x, y), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, self.audio_manager, "O")
                if col == "lu":
                    LetterPushable((x, y), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, self.audio_manager, "U")
                if col == "ly":
                    LetterPushable((x, y), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, self.audio_manager, "Y")
                    
    def checkpoint_1(self):
        if self.level > 0:
            return
        print("Checkpoint 1 reached")
        audio = pygame.mixer.Sound("./assets/audio/ghost/LightsOff.wav")
        self.ghost.PlayNext(audio)
        self.level_1_door.Close()
        self.player.glow_radius = 1.5
        self.level = 1
        
        for tourch in self.tourches:
            tourch.turn_off()
        
    def checkpoint_2(self):
        if self.level > 1:
            return
        print("Checkpoint 2 reached")
        self.player.glow_radius = 3
        for lava in self.lave:
            lava.turn_on()

        self.level = 2
        
    def checkpoint_3(self):
        if self.level > 2:
            return
        print("Checkpoint 3 reached")
        self.level3.isCompleted = True
        self.level3.door.Close()
         
    def turn_off_lava(self):
        for lave in self.lave:
            lave.turn_off()
            
        for tourch in self.tourches:
            tourch.turn_on()
    
    def change_player(self):
        self.player.change_to_knight()
    
    def MainMenueUpdate(self, events):
        self.mainMenu.run(events)
    
    def GameUpdate(self):
        # update and draw game
        self.visible_sprites.custom_draw(self.player, self.tourches)
        self.visible_sprites.update()
        self.audio_manager.update()
        self.ghost.update(pygame.time.get_ticks())
        if self.level == 2 and self.level3:
            self.level3.update()
            
    def WinUpdate(self):
        # draw a win screen "to be continued"
        self.display_surface.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text1 = font.render("You have escaped the hell-'o'.", True, 'white')
        text2 = font.render("Now you gonna climb up to the paradise-'o'.", True, 'white')
        text3 = font.render("To be continued... [ESCAPE HELLO 2].", True, 'white')
        
        self.display_surface.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2 - text1.get_height() // 2))
        self.display_surface.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + text2.get_height() // 2))
        self.display_surface.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT // 2 + text2.get_height() + text3.get_height() // 2))    
    
    def DeathUpdate(self, events):
        # draw a death screen
        self.display_surface.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("You died", True, 'white')
        text2 = font.render("Press R to restart", True, 'white')
        
        self.display_surface.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        self.display_surface.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + text2.get_height() // 2))
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart()
    
    def run(self, events):
        if self.game_state == 0:
            self.MainMenueUpdate(events)
        if self.game_state == 1:
            self.GameUpdate()
        if self.game_state == 2:
            self.WinUpdate()
        if self.game_state == 3:
            self.DeathUpdate(events)
        
    def finish(self):
        if self.finished:
            return
        self.finished = True
        self.player.canMove = False
        self.game_state = 2
    
    def die(self):
        self.game_state = 3
        
    def restart(self):
        # restart the actual level
        self.done = True
          
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_with = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        self.map_surface = pygame.Surface(self.display_surface.get_size())
        

    def custom_draw(self, player: Player, tourches: list):
        if player is None:
            return
        
        
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_with
        self.offset.y = player.rect.centery - self.half_height
        
        sprites_to_draw = []

        self.map_surface.fill((0, 0, 0))

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_post = sprite.rect.topleft - self.offset
            sprites_to_draw.append((sprite, offset_post))
            
        # sort by the order
        sprites_to_draw.sort(key = lambda sprite: sprite[0].order)
        
        for sprite, offset_post in sprites_to_draw:
            self.map_surface.blit(sprite.image, offset_post)
            
        glow_surf = player.generate_glow((255, 255, 255), 255)
        r = player.get_glow_radius()
        # put the glow surface on the display surface at the player's position
        self.display_surface.blit(glow_surf, (self.half_with - TILESIZE * r, self.half_height - TILESIZE * r))
        
        # tourches
        for tourch in tourches:
            if not tourch.isFlame:
                continue
            x = tourch.rect.centerx - self.offset.x
            y = tourch.rect.centery - self.offset.y
            r = tourch.get_radius()
            glow_surf = tourch.generate_glow((255, 200, 200), 255)
            self.display_surface.blit(glow_surf, (x - TILESIZE * r, y - TILESIZE * r))
        
        # blend the glow surface with the original surface
        self.display_surface.blit(self.map_surface, (0, 0), special_flags = pygame.BLEND_RGBA_MULT)