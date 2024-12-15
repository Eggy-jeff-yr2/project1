# road.py
import pygame


class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'assets/images/road.png')
        self.image1 = pygame.image.load(r'assets/images/road.png')
        self.rect = self.image.get_rect()
        self.rect1 = self.image1.get_rect()
        surface = pygame.display.get_surface()
        self.rect.bottomleft = surface.get_rect().bottomleft
        self.rect.y += 25
        self.rect1.bottomleft = self.rect.bottomright

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)

    def update(self):
        self.rect.x -= 2
        self.rect1.x -= 2
        if self.rect.right < 0:
            self.rect.left = self.rect1.right
        if self.rect1.right < 0:
            self.rect1.left = self.rect.right


