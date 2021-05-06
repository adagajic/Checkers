import pygame

from tabla import Tabla
from minmax import minmax
pygame.init()
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
size = (800, 800)
clock = pygame.time.Clock()
light = (170,170,170)
dark = (100,100,100)
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers")
done = False
GUI = True
komp = False
tabla = Tabla()
font1=pygame.font.SysFont('Corbel',70)
tabla.drawBoard(screen)
def btton(screen,x,y,text,color):
    pygame.draw.rect(screen,color,[x,y,400,100])
    text_rect = text.get_rect(center = (screen_width//2,y+50))
    screen.blit(text,text_rect)

while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and not GUI:
            pos=pygame.mouse.get_pos()
            x,y=pos
            tabla.position(x,y,screen)
        if event.type == pygame.MOUSEBUTTONDOWN and GUI:
            pos = pygame.mouse.get_pos()
            x,y = pos
            if x>200 and x<400 and y>200 and y<300:
                GUI = False
            if x>200 and x<400 and y>500 and y<600:
                GUI = False
                komp = True

    screen.fill(WHITE)
    if GUI:
        text1 = font1.render('Igrac', True, WHITE)
        text2 = font1.render('Kompjuter', True, WHITE)
        pos = pygame.mouse.get_pos()
        x, y = pos
        if x>200 and x<400 and y>200 and y<300:
            btton(screen,200,200,text1,light)
            btton(screen,200,500,text2,dark)
        elif x>200 and x<400 and y>500 and y<600:
            btton(screen, 200, 200, text1, dark)
            btton(screen, 200, 500, text2, light)
        else:
            btton(screen, 200, 200, text1, dark)
            btton(screen, 200, 500, text2, dark)
    if not GUI:
        tabla.drawBoard1(screen)
        pygame.display.flip()
        if tabla.turn==WHITE and komp:

            tr=minmax(4,tabla)

            tabla.drawBoard1(screen)

        if tabla.pobeda():
            done = True


    pygame.display.flip()
    clock.tick(60)
pygame.quit()
