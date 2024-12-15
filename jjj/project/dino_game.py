# main.py
import pygame
import sys
from assets.sprites.road import Road
from assets.sprites.clouds import Cloud
from assets.sprites.dino import Dino
from assets.sprites.obstacles import Cactus
from assets.sprites.score import Score
from assets.sprites.gameover import GameOver

pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
FPS = 60

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")
clock = pygame.time.Clock()


# Sprites and Game Variables
def main():
    road = Road()
    clouds = pygame.sprite.Group()
    player = Dino()
    obstacles = pygame.sprite.Group()
    score = Score()
    gameover = False

    # Game loop
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and gameover:
                    main()

        # Check for collisions
        for obstacle in obstacles:
            if pygame.sprite.collide_mask(player, obstacle) and not gameover:
                gameover = True
                end = GameOver()

        # Render
        screen.fill((255, 255, 255))
        road.draw(screen)
        clouds.draw(screen)
        player.draw(screen)
        obstacles.draw(screen)
        score.draw(screen)

        # Render Game Over if game ends
        if gameover:
            end.draw(screen)

        # Update sprites only if game is active
        if not gameover:
            player.update()
            road.update()
            clouds.update()
            obstacles.update()
            score.update(player.step)

        if len(obstacles) < 1:
            obstacles.add(Cactus())
        if len(clouds) < 3:
            clouds.add(Cloud())

        pygame.display.update()


if __name__ == "__main__":
    main()
