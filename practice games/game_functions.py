import sys

import pygame

from dog import Rocco
#from cat import Cats

def check_events(dog):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, dog)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, dog)
            

        
def check_keydown_events(event, dog):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        dog.moving_right = True
    elif event.key == pygame.K_LEFT:
        dog.moving_left = True
    elif event.key == pygame.K_UP:
        dog.moving_up = True
    elif event.key == pygame.K_DOWN:
        dog.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, dog):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        dog.moving_right = False
    elif event.key == pygame.K_LEFT:
        dog.moving_left = False
    elif event.key == pygame.K_UP:
        dog.moving_up = False
    elif event.key == pygame.K_DOWN:
        dog.moving_down = False
        
def update_screen(settings, screen, dog, cat):
    #Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
 
    dog.blitme()
    cat.blitme()
    
    #Make the most recently drawn screen visible.
    pygame.display.flip()
        
        

