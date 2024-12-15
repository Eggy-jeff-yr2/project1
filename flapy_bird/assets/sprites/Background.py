import pygame

class City(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/city.png")
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.center = surface.get_rect().center


    def draw(self, surface):
        surface.blit(self.image, self.rect)

