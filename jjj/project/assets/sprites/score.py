# game.py
import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.step = 0
        self.font = pygame.font.Font(r"assets\font\gamefont.ttf", 20)
        self.image = self.font.render(f'Score: {self.points}', True, (83, 83, 83))
        self.rect = self.image.get_rect(topright=(550 - 10, 10))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f"HI {self.points}", True, (83, 83, 83))

    def update(self, steps):
        if steps%10 == 0 and steps >= 0:
            self.points += 1
