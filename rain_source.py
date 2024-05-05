import pygame
from pygame.sprite import Sprite 
import random


class Raindrop(Sprite):
   
    """Create Sprite of Raindrop"""
    def __init__(self, rain):
        """Initialize attributes"""
        super().__init__()
        self.screen = rain.screen
        self.raindrop_speed = random.randrange(5,10)
        self.image = pygame.image.load("Raindrop.png")
        self.rect = self.image.get_rect()

        """WIDTH AND HEIGHT"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        
    

    def update(self):
        """Raindrop Sprite Moves Downward"""
        self.y += self.raindrop_speed
        self.y = self.rect.y 

    def check_edges(self): 
        """If the raindrop reaches the bottom of the screen cause the raindrop to reposition"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom: 
            return True 
       
   


 