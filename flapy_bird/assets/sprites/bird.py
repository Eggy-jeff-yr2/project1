import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load(r"assets\images\bird1.png")
        self.image2 = pygame.image.load(r"assets\images\bird2.png")
        self.image3 = pygame.image.load(r"assets\images\bird3.png")
        self.sound_wing = pygame.mixer.Sound(r"assets\sounds\wing.wav")
        self.point_gain = pygame.mixer.Sound(R"assets\sounds\point.wav")
        self.images = [self.image1, self.image2, self.image3]
        self.image = self.image1
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.center = surface.get_rect().center
        self.rect.x -= 75
        self.step = 0
        self.gravity = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.step += 1
        if self.step % 7 == 0:
            self.images = [*self.images[1:], self.images[0]]
            self.image = pygame.transform.rotate(self.images[0], -self.gravity * 5)
        self.gravity += 0.25
        self.rect.y += self.gravity
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.gravity > 0:
            self.gravity -= 7
            self.sound_wing.play()