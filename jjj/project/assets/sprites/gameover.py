import pygame

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(r"assets\font\gamefont.ttf", 30)
        self.image = self.font.render('Game Over', True, (83, 83, 83))
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.x = surface.get_width() // 4
        self.rect.y = surface.get_height() // 4
        self.image1 = pygame.image.load(r"assets\images\reset.png")
        self.rect1 = self.image1.get_rect()
        self.rect1.x = surface.get_height() // 2.1
        self.rect1.y = surface.get_height() // 3


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)