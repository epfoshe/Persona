import pygame
from pygame.sprite import Sprite 
import random


class Raindrop(Sprite):
   
    """Create Sprite of Raindrop"""
    def __init__(self, rain_grid):
        """Initialize attributes"""
        super().__init__()
        self.screen = rain_grid.screen
        self.raindrop_speed = random.randrange(5,10)
        self.image = pygame.image.load("raindrop_2.png")
        self.rect = self.image.get_rect()
        self.speed = random.randrange(10, 20)

        """WIDTH AND HEIGHT"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        
    

    def update(self):
        """Raindrop Sprite Moves Downward"""
        self.y += self.raindrop_speed 
        self.rect.y = self.y

    def check_edges(self): 
        """If the raindrop reaches the bottom of the screen cause the raindrop to reposition"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom: 
            return True
        
       
   


 