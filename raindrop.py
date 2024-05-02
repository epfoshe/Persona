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
        self.rect.x = self.rectangle.width 
        self.rect.y = self.rectangle.height 

        """float?"""
    

    def update(self):
        """Raindrop Sprite Moves Downward"""
        self.y += self.raindrop_speed
        self.rectangle.y = self.y

    def check_edges(self):
        """Bottom of the screen"""
        screen_rectangle = self.screen.get_rect() 
        return self.rect.bottom > screen_rectangle.bottom


 