import pygame

class Rocco():
    
    def __init__(self, settings, screen):
        """Initialize the dog and set its starting position."""
        self.screen = screen
        
        self.settings = settings
        
        #Load the dog image and get its rect.
        self.image = pygame.image.load('images/greyhound.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        
        #Start each new dog in the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        #Store a decimal value for the dog's center.
        self.center1 = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center1 += self.settings.dog_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center1 -= self.settings.dog_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.center2 -= self.settings.dog_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center2 += self.settings.dog_speed_factor
        
        #Update rect object from self.center
        self.rect.centerx = self.center1
        self.rect.centery = self.center2
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    
