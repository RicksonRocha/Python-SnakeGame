import pygame
from pygame.locals import *
import random

window_size = (600, 600)
pixel_size = 10

pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake')

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((pixel_size, pixel_size))  # quadradinho branco
snake_surface.fill((255, 255, 255))  # snake color
snake_direction = K_LEFT

apple_surface = pygame.Surface((pixel_size, pixel_size))
apple_surface.fill((255, 0, 0))


def collision(pos1, pos2):
    return pos1 == pos2


def off_limits(pos):
    if 0 <= pos[0] < window_size[0] and 0 <= pos[1] < window_size[1]:
        return False
    else:
        return True


def apple_on_grid():
    x = random.randint(0, window_size[0])
    y = random.randint(0, window_size[1])
    return x // pixel_size * pixel_size, y // pixel_size * pixel_size

def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = apple_on_grid()

apple_pos = apple_on_grid()

while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:  # pygame.locals.QUIT
           restart_game()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(apple_surface, apple_pos)

    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = apple_on_grid()

    for pos in snake_pos:
        screen.blit(snake_surface, pos)  # desenha os pixels na tela

    # corpo acompanha a cebeça
    for i in range(len(snake_pos) - 1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
           restart_game()
        snake_pos[i] = snake_pos[i - 1]

    # checa os limites
    if off_limits(snake_pos[0]):
        restart_game()

    # movimenta a cabeça da cobrinha
    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - pixel_size)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + pixel_size)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - pixel_size, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + pixel_size, snake_pos[0][1])

    pygame.display.update()  # atualiza a tela com a função blit
