import pygame
import pygame.sprite import Sprite
import random

class Raindrop(Sprite):
    """Create Sprite of Raindrop"""
    def __init__(self, rain):
        """Initialize attributes"""
        super().__init__()
        self.screen = rain.screen
        self.raindrop_speed = random.randrange(1,10)

        """Load Image into VSC"""

        """WIDTH AND HEIGHT"""
    def update(self):
        """Raindrop Sprite Moves Downward"""
 