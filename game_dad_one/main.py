import pygame

pygame.init()

# Window creation
screen = pygame.display.set_mode((412, 512))
pygame.display.set_caption("ball_game")

ball_speed = [5, 5]
ball_pos = [100, 100]

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[0] <= 0 or ball_pos[0] >= 412:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= 0 or ball_pos[1] >= 512:
        ball_speed[1] = -ball_speed[1]

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), ball_pos, 5)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
