import pygame
from pygame.sprite import Sprite

class Cats(Sprite):

    def __init__(self, settings,screen):
        super(Cats, self).__init__()
        self.screen = screen
        self.settings = settings
        
        #Load the cat image and get its rect.
        self.image = pygame.image.load('images/cat.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new cat
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        
        #Store cat's exact position.
        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image, self.rect) 
