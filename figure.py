import pygame

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
size = (800, 800)
crown = pygame.transform.scale(pygame.image.load('crown-512.png'),(32,32))

class Figura:
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.king = False
        self.centerx = column * 100 + 50
        self.centery = row * 100 + 50


    def drawcircle(self, screen):
        pygame.draw.circle(screen, self.color, (self.centerx, self.centery), 35)
        if self.king:
            screen.blit(crown,(self.centerx-16,self.centery-16))

    def movepiece(self, row, column):
        self.row = row
        self.column = column
        self.centerx = column * 100 + 50
        self.centery = row * 100 + 50