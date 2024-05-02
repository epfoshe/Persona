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

        """Set Main Background"""
        pygame.image.load("jason_scheier_raining.jpg").convert

        """Create Grouping Together"""
        self.raindrop = pygame.sprite.RenderPlain

        #Add music and rain?
        self.music()
      
    def music(self):
        """Create Background Music"""
        #ADD TRADITIONAL MUSIC .("musicfile.wav")
        pygame.mixer.music.load()
        pygame.mixer.music.set_volume(.2)
        pygame.mixer.music.play


    def Rain(self):
        """Loop Rain Object"""





    def _check_events_thunder(self):
        """Add Thunder Game Loops """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
           
           #Q to quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()

            #Activate key to start thunder ("thunder.wav")

            elif event.type == pygame.K_SLASH:
                pygame.mixer.music.load()
                pygame.image.load()
                pygame.mixer.music.play


            #Activate key to start thunder ("thunder.wav")                   


    def _create_rain(self):
        """dd"""
    
    def _update_rain(self):
        """ss"""
    
    def _change_pos(self):
        """sss"""
    
    def _update_(self):
        """ddd"""





if __name__ == "__main__": 
    ra = Rain_action()
    ra.Rain