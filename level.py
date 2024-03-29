import pygame
from settings import *
from entities.tiles import Ground, Wall, TestInteractable, Chest, GoldenChest, LeftWall,BottomLeft,TopLeft,BottomRight,TopRight,RightWall,BottomWall,TopWall,TopRightCorner,TopLeftCorner
from entities.player import Player

class Level:
    def __init__(self):
        # get the display surface 
        self.display_surface = pygame.display.get_surface()
    

        # sprite group set up
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.interactable_sprites = pygame.sprite.Group()
        self.background_sprites = pygame.sprite.Group()

        # sprite set up
        self.create_map()

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
                if col ==  "TRC":
                    TopRightCorner((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue
                if col ==  "TLC":
                    TopLeftCorner((x,y),[self.visible_sprites, self.obstacle_sprites])
                    continue

                Ground((x, y), [self.visible_sprites, self.background_sprites])

                if col == "BL":
                    BottomLeft((x,y),[self.visible_sprites, self.obstacle_sprites])          
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
                if col == "t":
                    TestInteractable((x, y), [self.visible_sprites, self.interactable_sprites])
                if col == "c":
                    Chest((x, y), [self.visible_sprites, self.interactable_sprites])
                if col == "g":
                    GoldenChest((x, y), [self.visible_sprites, self.interactable_sprites])
                

    def run(self):
        # update and draw game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_with = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        if player is None:
            return
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_with
        self.offset.y = player.rect.centery - self.half_height
        
        sprites_to_draw = []

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_post = sprite.rect.topleft - self.offset
            sprites_to_draw.append((sprite, offset_post))
            
        # sort by the order
        sprites_to_draw.sort(key = lambda sprite: sprite[0].order)
        
        for sprite, offset_post in sprites_to_draw:
            self.display_surface.blit(sprite.image, offset_post)