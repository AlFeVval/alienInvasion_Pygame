import pygame

class Ship():

    def __init__(self,ai_settings, screen):
        """ Initialize the ship and set its position """
        self.screen = screen
        self.width = 50
        self.height = 50
        
        self.ai_settings = ai_settings

        #Load the ship image and get its rect
        og_img = pygame.image.load('sprites/ship.png')
        self.image = pygame.transform.scale(og_img, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Start new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Decimal value of center reference
        self.center = float(self.rect.centerx)

        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """ Draw the ship at the current location """
        self.screen.blit(self.image, self.rect)