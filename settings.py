'''
Description: 
Author: Andy An
Date: 2021-10-12 18:05:28
LastEditors: Andy An
LastEditTime: 2021-11-01 20:38:06
FilePath: \alien-invasion\settings.py
'''
class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game settings"""
        # Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color =(230,230,230)
        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color =(60,60,60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed= 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; - 1 represents left
        self.fleet_direction = 1
        