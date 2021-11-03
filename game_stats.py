'''
Description: 
Author: Andy An
Date: 2021-11-01 21:42:12
LastEditors: Andy An
LastEditTime: 2021-11-03 19:05:06
FilePath: \alien-invasion\game_stats.py
'''
class GameStats:
    """ Track statistics for Alien Invasion"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an false state
        self.game_active = False

        # High score should never be reset 
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left= self.settings.ship_limit
        self.score = 0
        self.level = 1
        
        
