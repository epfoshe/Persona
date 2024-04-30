import random
import pygame

from raindrop import Raindrop
from PIL import Image 

class Rain_action():
    def __init__(self):
        pygame.init

        """Create Screen"""
        ##STORE INTO SOMETHING
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width 
        self.screen_height = self.screen.get_rect().height 

        """Set the caption"""
        pygame.display.set_caption("Rain_action")

        """Create Grouping Together"""
        self.raindrop = pygame.sprite.RenderPlain

        #Add music and rain?

    def Rain(self):
        """Loop Rain Object"""

    def music(self):
        """Create Background Music"""

    def _check_events(self):
        """distinguish updates """




if __name__ == "__main__": 
    ra = Rain_action()
    ra.Rain