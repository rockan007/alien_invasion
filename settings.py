'''
Description: 
Author: Andy An
Date: 2021-10-12 18:05:28
LastEditors: Andy An
LastEditTime: 2021-10-13 17:22:28
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

        self.ship_speed = 1.5
        