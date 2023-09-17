import sys

import pygame

from settings import Settings
from clock import Clock


class Program:
    """Klasa główna programu."""

    def __init__(self):
        pygame.init()
        self.running = True
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption(self.settings.title)

        self.clock = Clock(self)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i myszkę."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False

    def _update_screen(self):
        """Odświeżanie ekranu."""
        self.screen.fill((55, 88, 22))
        pygame.display.flip()

    def run(self):
        """Główna pętla programu."""
        while self.running:
            self._check_events()
            self._update_screen()
            self.clock.tick_clock()
