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
        self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
        self.rect.y = random.randint(-self.rect.height, -5)

        """float?"""
    

    def update(self):
        """Raindrop Sprite Moves Downward"""
        self.rect.y += self.raindrop_speed
        if self.rect.y > self.screen.get_height():
            self.rect.y = random.randint(-self.rect.height, -5)
            self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)

   


 