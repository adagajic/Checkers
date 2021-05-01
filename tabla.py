import numpy as np
import pygame

from figure import Figura
WHITE = (255,255,255)
GREEN = (0,255,0)
RED   = (255,0,0)
BLACK = (0,0,0)
size = (800,800)
class Tabla:
    def __init__(self):
        self.board = np.full((8,8),Figura(0,0,GREEN))
        self.moveturn = False
        self.turn = RED


    def drawBoard(self,screen):
        for row in range(8):
            for column in range(8):
                if (row+column)%2==0:
                    pygame.draw.rect(screen,WHITE,[column*100,row*100,100,100])
                else:
                    pygame.draw.rect(screen,GREEN,[column*100,row*100,100,100])
                    if row<3:
                        self.board[row][column]=(Figura(row,column,WHITE))
                        fig = self.board[row][column]
                        fig.drawcircle(screen)
                    if row>4:
                        self.board[row][column] = Figura(row,column,RED)
                        fig = self.board[row][column]
                        fig.drawcircle(screen)
    def getColor(self,x,y):
        column=x//100
        row=y//100
        return self.board[row][column].color


    def position(self,x,y):
        if self.moveturn:
            blcon=move(x,y)
            if not blcon:
                self.moveturn=False
                self.position(x,y)
        if self.getColor(x,y)==RED:
            self.moveturn=True
            self.validTurns=self.getValidMoves(x,y)
