import sys
import pygame
from settings import *

class Option:
    hovered = False
    def __init__(self, text, pos, font):
        self.text = text
        self.pos = pos
        self.font = font
        self.set_rect()
        #self.draw()
        
            
    def draw(self, screen):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = self.font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

class MainMenu:
    def __init__(self, new_game):
        self.font = pygame.font.Font(None, 40)
        
        new_game_pos = (WIDTH // 2 - 100, HEIGHT // 2 - 100)
        #options_pos = (WIDTH // 2 - 100, HEIGHT // 2 - 50)
        quit_pos = (WIDTH // 2 - 100, HEIGHT // 2 - 50)
        
        self.options = [Option("START GAME", new_game_pos, self.font),
                        #Option("OPTIONS", options_pos, self.font),
                        Option("QUIT", quit_pos, self.font)]
        
        self.new_game = new_game
        #self.options = options
        self.quit = self.quit
        
        # get py game screen
        self.screen = pygame.display.get_surface()
        
    def quit(self):
        pygame.quit()
        sys.exit()
        
    def run(self, events):
        self.screen.fill((0, 0, 0))
        for option in self.options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            option.draw(self.screen)
            
        for event in events:
            # if the event is a click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for option in self.options:
                    if option.rect.collidepoint(pygame.mouse.get_pos()):
                        if option.text == "START GAME":
                            self.new_game()
                        elif option.text == "OPTIONS":
                            self.options()
                        elif option.text == "QUIT":
                            self.quit()
            
        pygame.display.update()
        