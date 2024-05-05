import random
import pygame

from rain_source import Raindrop
from pygame.locals import *

class Rain_action():
    def __init__(self):
        pygame.init()

        """Create Screen"""
        self.screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        """Set the caption"""
        pygame.display.set_caption("Rain_action")

        """Set Main Background"""
        self.background_image = pygame.image.load("jason_scheier_raining.jpg").convert()

        """Create Grouping Together"""
        self.raindrops = pygame.sprite.Group()

        """Preparing for Frame Rate"""
        self.clock = pygame.time.Clock()

        # Add music and rain?
        pygame.mixer.init()
        self.music()
        self._create_rain()

    def music(self):
        """Create Background Music"""
        pygame.mixer.music.load("rain_sounds.wav")
        pygame.mixer.music.set_volume(0.2)
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

            # Q to quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()

            # Activate key to start thunder ("thunder.wav")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SLASH:
                pygame.mixer.music.load("sound_thunder.wav")
                pygame.mixer.music.play()

    def _create_rain(self, row_number, drop_amount):
        """Link raindrop.py to thunder.py
        Then find the horizontal space for the rain particle per row
        Then find the vertical space (y) and number of rows
        Create a loop"""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        drop_number = self.screen_width // (2 * raindrop_width)

        number_row = self.screen_height // (2 * raindrop_height)

        # Create loop for the rain grid
        for row_number in range(number_row):
            for drop_amount in range(drop_number):
                self._create_raindrops(row_number, drop_amount)

    def _create_raindrops(self):
        """Creates the actual raindrop in the screen"""
        raindrop = Raindrop(self)

        # Randomly choose placement for the raindrops
        raindrop.x = random.randrange(0, self.screen_width)
        raindrop.rect.x = raindrop.x
        raindrop.y = random.randrange(0, self.screen_height)
        self.raindrops.add(raindrop)

    def _update_rain(self):
        """Update the rain position"""
        self.raindrops.update()

        for raindrop in self.raindrops.sprites():
            if raindrop.check_edges():
                self._change_pos(raindrop)

    def _change_pos(self, raindrop):
        """Changes the position of the raindrop to the top of the screen"""
        raindrop.rect.y = 0

    def _update_screen(self):
        """Screen updates to display actual rain
        Draws raindrops in and flips the display"""
        self.screen.blit(self.background_image, (0, 0))
        self.raindrops.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(30)  # Limit to 30 frames per second

if __name__ == "__main__":
    ra = Rain_action()
    ra.Rain()
