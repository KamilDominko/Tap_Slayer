import sys

import pygame

from player import Player


class Game:
    """Klasa główna gry."""

    def __init__(self, program):
        self.running = True
        self.settings = program.settings
        self.clock = program.clock
        self.screen = program.screen
        self.bg_image = pygame.image.load("images/game_bg.bmp")

        self.player = Player(self)

        self.mouse_l = False
        self.mouse_r = False

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i myszkę."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_l = True
                elif event.button == 3:
                    self.mouse_r = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_l = False
                elif event.button == 3:
                    self.mouse_r = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False

    def _update_screen(self):
        """Odświeżanie ekranu."""
        self.screen.blit(self.bg_image, (0, 0))
        self.player.blitme()
        pygame.display.flip()

    def run(self):
        """Główna pętla programu."""
        while self.running:
            self._check_events()
            self.player.update()
            self._update_screen()
            self.clock.tick_clock()
