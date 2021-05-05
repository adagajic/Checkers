import pygame
import time
from tabla import Tabla
from minmax import minmax
pygame.init()
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
size = (800, 800)
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers")
done = False
tabla = Tabla()
tabla.drawBoard(screen)
while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            x,y=pos
            tabla.position(x,y,screen)

    screen.fill(WHITE)
    tabla.drawBoard1(screen)
    pygame.display.flip()
    if tabla.turn==WHITE:

        tr=minmax(4,tabla)

        tabla.drawBoard1(screen)

    if tabla.pobeda():
        done = True
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
