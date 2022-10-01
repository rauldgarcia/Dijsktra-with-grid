import pygame
import dijkstra
import numpy as np
 
AZUL = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN= (0, 255, 0)
tamCuadro = 40

pygame.init()
size = (123, 123)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
gameOver = False
wmat = [[0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 0]]

camino=(dijkstra.find_shortest_path(wmat,0,8))
print(camino)
print(dijkstra.find_shortest_distance(wmat,0,8))

x=[1,42,83,1,42,83,1,42,83]
y=[1,1,1,42,42,42,83,83,83]

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(BLACK)
    for i in range(1, size[0], tamCuadro + 1):
        for j in range(1, size[1], tamCuadro + 1):
            pygame.draw.rect(screen, AZUL, [i, j, tamCuadro, tamCuadro], 0)
    pygame.display.flip()
    pygame.time.delay(1000)
    pygame.draw.rect(screen, RED, [x[0], y[0], tamCuadro, tamCuadro], 0)
    pygame.draw.rect(screen, RED, [x[8], y[8], tamCuadro, tamCuadro], 0)
    pygame.display.flip()
    pygame.time.delay(1000)
    for i in camino:
        pygame.draw.rect(screen, GREEN, [x[i], y[i], tamCuadro, tamCuadro], 0)
        pygame.display.flip()
        pygame.time.delay(1000)
    gameOver = True
pygame.quit()
