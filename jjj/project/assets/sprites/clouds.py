import pygame
import random


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'assets/images/cloud.png')
        self.rect = self.image.get_rect()
        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()
        surface = pygame.display.get_surface()
        self.rect.x = surface.get_width()
        self.rect.y = random.randint(0, surface.get_height() // 2 - self.rect.height)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= random.randint(2, 5)
        if self.rect.right < 0:
            self.kill()
