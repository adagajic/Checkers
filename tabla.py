import pygame
from .figure import Figura
pygame.init()
WHITE = (255,255,255)
GREEN = (0,255,0)
RED   = (255,0,0)
BLACK = (0,0,0)
size = (800,800)
class Tabla:
    def __init__(self):
        self.board = [][]
    def drawBoard(self,screen):
        for row in range(8):
            for column in range(8):
                if (row+column)%2==0:
                    pygame.draw.rect(screen,WHITE,[column*100,row*100,100,100])
                else:
                    pygame.draw.rect(screen,GREEN,[column*100,row*100,100,100])
                    if row<3:
                        self.board[row][column] = Figura(row,column,WHITE)
                        fig = self.board[row][column]
                        fig.drawcircle(screen)
                    if row>4
                        self.board[row][column] = Figura(row,column,BLACK)
                        fig = self.board[row][column]
                        fig.drawcircle(screen)

