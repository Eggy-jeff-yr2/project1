import pygame
import sys
from assets.sprites.Background import City
from assets.sprites.road import Road
from assets.sprites.bird import Bird
from assets.sprites.pipes import Pipe
from assets.sprites.game import Score

pygame.init()

# Constants
WIDTH = 288
HEIGHT = 512
FPS = 60

# Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()


def main():
    # Sprites
    city = City()
    road = Road()
    player = Bird()
    pipes = pygame.sprite.Group()
    score = Score()
    pipes.add(Pipe())

    game_over = False
    checkpoint = False
    running = True
    while running:
        # Screen refresh rate
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for pipe in pipes:
            if (pipe.rect1.collidepoint(player.rect.midbottom) or pipe.rect2.collidepoint(player.rect.midtop)) and not game_over:
                game_over = True

        if (player.rect.colliderect(road.rect) or player.rect.colliderect(road.rect1)) and not game_over:
            game_over = True

        if player.rect.top <= 0 and not game_over:
            game_over = True

        if pipes.sprites()[0].rect1.x < player.rect.x and not checkpoint:
            score.points += 1
            checkpoint = True
            player.point_gain.play()

        # Rendering
        city.draw(screen)
        for i in pipes:
            i.draw(screen)
        road.draw(screen)
        player.draw(screen)
        score.draw(screen)

        # Updating sprites
        if not game_over:
            road.update()
            player.update()
            pipes.update()
        score.update()
        if len(pipes) < 1:
            pipes.add(Pipe())
            checkpoint = False

        # Screen Refresh
        pygame.display.update()


if __name__ == "__main__":
    main()
