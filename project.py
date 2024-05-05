import random
import pygame

from rain_source import Raindrop
from pygame.locals import *

class Rain_action():
    def __init__(self):
        pygame.init
        

        """Create Screen"""
        ##STORE INTO SOMETHING
        self.screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width 
        self.screen_height = self.screen.get_rect().height 

        """Set the caption"""
        pygame.display.set_caption("Rain_action")

        """Set Main Background"""
        self.background_image = pygame.image.load("jason_scheier_raining.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, ((1920, 1080)))

        """Create Grouping Together"""
        self.raindrops = pygame.sprite.RenderPlain

        """Preparing for Frame Rate"""
        self.clock = pygame.time.Clock()

        #Add music and rain?
        pygame.mixer.init()
        self.music()
        self._create_rain
      
    def music(self):
        """Create Background Music"""
        #ADD TRADITIONAL MUSIC .("musicfile.wav")
        pygame.mixer.music.load("rain_sounds.wav")
        pygame.mixer.music.set_volume(.2)
        pygame.mixer.music.play(-1)


    def Rain(self):
        """Loop Rain Object for the Infinite Effect"""
        while True:
            self._check_events_thunder()
            self._update_rain()
            self._update_screen()
    





    def _check_events_thunder(self):
        """Add Thunder Game Loops """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
           
           #Q to quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()

            #Activate key to start thunder ("thunder.wav")

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SLASH:
                    #ADD THUNDER SOUND EFFECT
                    pygame.mixer.music.load("sound_thunder.wav")
                    pygame.mixer.music.play()
                    self.background_image = pygame.image.load("jason_scheier_thunder.jpg").convert()
                    self.background_image = pygame.transform.scale(self.background_image, (1920 , 1080))

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SLASH:
                    self.background_image = pygame.image.load ("jason_scheier_raining.jpg").convert()
                    self.background_image = pygame.transform.scale(self.background_image, (1920 , 1080))
                    pygame.mixer.music.load("rain_sounds.wav")
                    pygame.mixer.music.play()
            #Activate key to start thunder ("thunder.wav")    
                           


    def _create_rain(self):
        """Link raindrop.py to thunder.py
        Then find the horizontal space for the rain particle per row
        Then find the vertical space (y) and number of rows 
        Create a loop"""
        #Think like a grid method we learned 
        raindrop = Raindrop(self)
        raindrop_width , raindrop_height = raindrop.rect.size
        drop_number = self.screen_width // (4 * raindrop_width)

        number_row = self.screen_height // (4 * raindrop_height)

        #Create loop for the rain grid
        for row_number in range(number_row):
            for drop_amount in range(drop_number):
                self._create_raindrops(row_number, drop_amount)
        
        raindrop.x = random.randrange(0, self.screen_width)
        raindrop.rect.x = raindrop.x
        raindrop.y = random.randrange(0, self.screen_height)
        raindrop.rect.y =  raindrop.y
        self.raindrops.add(raindrop)

        self.raindrops.add(raindrop)






    def _create_raindrops(self):
        """Creates the actual raindrop in the screen"""
        raindrop = Raindrop(self)
        
        #Randomly choose placement for the raindrops
        raindrop.x = random.randrange(0, self.screen_width)
        raindrop.rect.x = raindrop.x 
        raindrop.y = random.randrange(0, self.screen_height)
        self.raindrop.add(raindrop)





    def _update_rain(self):
        """Update the rain position"""
        self.raindrops.update()

        for _raindrops in self.raindrops.sprites():
           if _raindrops.check_edges():
            self._change_pos
            
    
    def _change_pos(self, _raindrops):
        """Changes the position of the raindrop to the top of the screen"""
        _raindrops.y = 0 


    
    def _update_screen(self):
        """Screen updates to display actual rain
        Draws raindrops in and flips the display"""
        self.raindrops.draw(self.screen)
        pygame.display.flip()
        







if __name__ == "__main__": 
    ra = Rain_action()
    ra.Rain