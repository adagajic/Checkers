import pygame

from tabla import Tabla
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
while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            x,y=pos
            tabla.position(x,y)
    screen.fill(WHITE)
    tabla.drawBoard(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
