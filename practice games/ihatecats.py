import pygame

from dog import Rocco
from cat import Cats

from settings import Settings
import game_functions as gf

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, 
            settings.screen_height))
    pygame.display.set_caption("Rocco's nightmare.")
    
    #Make a Rocco
    dog = Rocco(settings, screen)

    #Make a Cat
    cat = Cats(settings, screen)
    
    #Start the main loop for the game.
    while True:
        
        #Watch for keyboard and mouse events.
        gf.check_events(dog)
        dog.update()
        
        #Redraw the screen during each pass through the loop.
        gf.update_screen(settings, screen, dog, cat)
run_game()
    
 
