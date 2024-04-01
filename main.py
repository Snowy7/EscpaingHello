import pygame, sys # importing the pygame and system libraries
from settings import * # importing the settings from the settings file
from level import Level # Level is the main class that will be running the game

# NO NEED TO EDIT
# BE SAFE PLEASE

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        # todo: GAME ICONs
        
        self.clock = pygame.time.Clock()
        self.level = Level()
        
    def run(self):
        # while True: to keep it running until the user quits
        while True:
            # hazard: this handles the game quit buttons (do not remove)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('#1c1117') # rgb(28, 17, 23)
            self.level.run(events)
            pygame.display.update()
            self.clock.tick(FPS) 
            
            if self.level.done:
                break
            
        self.Restart()

    def Restart(self):
        self.level = Level()
        self.run()

if __name__ == '__main__':
    game = Game()
    game.run()