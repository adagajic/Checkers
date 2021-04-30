import pygame
pygame.init()
WHITE = (255,255,255)
GREEN = (0,255,0)
RED   = (255,0,0)
BLACK = (0,0,0)
size = (800,800)
clock = pygame.time.Clock()

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Checkers")
done = False
clock = pygame.time.Clock()
while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                pygame.draw.rect(screen,WHITE,[i*100,j*100,100,100])
            else:
                pygame.draw.rect(screen,GREEN,[i*100,j*100,100,100])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()