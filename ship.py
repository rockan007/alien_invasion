'''
Description: 
Author: Andy An
Date: 2021-10-12 18:30:48
LastEditors: Andy An
LastEditTime: 2021-10-13 17:36:04
FilePath: \alien-invasion\ship.py
'''
import pygame

class Ship: 
    """A class to manage the ship"""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position"""
        # Assign the screen to an attribute of the ship
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Access the screen's rect attribute using the get_rect() method and assign it to self.screen_rect
        # Doing so allows us to place the ship in the correct location on the screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        # access the ship surface's rect attribute
        self.rect = self.image.get_rect()
        # Start each new shiip at the bottom of the screen.
        # Make the value of self.rect.midbottom match the midbottom attribute of the screen's rect
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        #Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update the ship'x value, not the rect.
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left> 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x
        # rect attributes such as x store only integer values
        self.rect.x = self.x
            
    def blitme(self):
        """Draw the ship at its current location"""
        # draws the image to the screen at the position specified by self.rect
        self.screen.blit(self.image,self.rect)