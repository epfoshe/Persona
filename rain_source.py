import pygame
import pygame.sprite import Sprite 
import random


class Raindrop(Sprite):
   
    """Create Sprite of Raindrop"""
    def __init__(self, rain):
        """Initialize attributes"""
        super().__init__()
        self.screen = rain.screen
        self.raindrop_speed = random.randrange(5,10)
        self.image = pygame.image.load("Raindrop.png")
        self.rectangle = self.image.get_rect()

        """WIDTH AND HEIGHT"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """float?"""
    

    def update(self):
        """Raindrop Sprite Moves Downward"""
        self.y += self.raindrop_speed
        self.y = self.rect.y 
       
   


 