import pygame

class Ship():

    def __init__(self, screen, width, height):
        """ Initialize the ship and set its position """
        self.screen = screen

        #Load the ship image and get its rect
        og_img = pygame.image.load('sprites/ship.png')
        self.image = pygame.transform.scale(og_img, (width, height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Start new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """ Draw the ship at the current location """
        self.screen.blit(self.image, self.rect)