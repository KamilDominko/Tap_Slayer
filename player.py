import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    """Klasa przeznaczona do reprezentwoania gracza na ekranie."""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load("images/player.bmp")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        # Pobierz aktualny y myszki i ustaw go na y gracza.
        mouse_pos = pygame.mouse.get_pos()
        self.rect.y = mouse_pos[1]
        # Sprawdź, czy gracz nie wyszedł za wysoko.
        if self.rect.top <= self.screen.get_height() // 4:
            self.rect.top = self.screen.get_height() // 4
        # Sprawdź, czy gracz nie wyszedł poniżej ekranu.
        if self.rect.bottom >= self.screen.get_height():
            self.rect.bottom = self.screen.get_height()

    def blitme(self):
        """Wyświetla gracza w jego aktualnym położeniu na ekranie."""
        self.screen.blit(self.image, self.rect)
