import pygame

pygame.init()
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
size = (800, 800)

class GameLogic:
    def __init__(self,row,column):
        self.row=row
        self.column=column

