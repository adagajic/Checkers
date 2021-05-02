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
        self.moveturn = None
        self.turn = RED
        self.validMoves = []
        self.skipped=False
        self.skippedPieces =[]

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
    def getPiece(self,x,y):
        column=x//100
        row=y//100
        return self.board[row][column]

    def move(self,x,y,screen):
        column = x // 100
        row = y // 100
        piece = self.board[row][column]
        if piece.color==GREEN and (row,column) in self.validMoves:
            piece2 = self.moveturn
            if self.skipped:
                for i in self.skippedPieces:
                    self.skippedPieces[i]
            else:
                self.board[row][column]=Figura(row,column,piece2.color)
                self.board[piece2.row][piece2.column]=Figura(piece2.row,piece2.column,GREEN)
                fig=self.board[row][column]
                fig.drawcircle(screen)
            return True
        return False
    def position(self,x,y,screen):
        piece = self.getPiece(x, y)
        if self.moveturn:
            blcon=self.move(x,y,screen)
            if not blcon:
                self.moveturn=None
                self.position(x,y,screen)


        elif piece.color==self.turn:
            column = x // 100
            row = y // 100
            self.moveturn=self.board[row][column]
            self.validMoves=self.getValidMoves(row,column)
    def getValidMoves(self,row,column):
        piece =self.board[row][column]
        color = piece.color

        if color == RED:
            piece1=self.board[row-1][column-1]
            piece2=self.board[row-1][column+1]
            if piece1.color==GREEN:
                self.validMoves.append((row - 1, column + 1))
            if piece2.color==GREEN:
                self.validMoves.append((row - 1, column + 1))
