import sys

import pygame


class Game:
    """Klasa główna gry."""

    def __init__(self, program):
        self.running = True
        self.settings = program.settings
        self.clock = program.clock
        self.screen = program.screen
        self.bg_image = pygame.image.load("images/game_bg.bmp")

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
        self.screen.blit(self.bg_image, (0, 0))
        pygame.display.flip()

    def run(self):
        """Główna pętla programu."""
        while self.running:
            self._check_events()
            self._update_screen()
            self.clock.tick_clock()
