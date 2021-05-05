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
        self.crvenef = 12
        self.belef = 12

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

    def drawBoard1(self,screen):
        for row in range(8):
            for column in range(8):
                if (row+column)%2==0:
                    pygame.draw.rect(screen,WHITE,[column*100,row*100,100,100])
                else:
                    pygame.draw.rect(screen,GREEN,[column*100,row*100,100,100])
                    fig=self.board[row][column]
                    if(fig.color==RED or fig.color==WHITE):
                        fig.drawcircle(screen)
    def getPiece(self,x,y):
        column=x//100
        row=y//100
        return self.board[row][column]
    def pobeda(self):
        if self.belef==0:
            print("Crveni je pobedio")
            return True
        if self.crvenef==0:
            print("Beli je pobedio")
            return True
        return False

    def move(self,x,y):
        column = x // 100
        row = y // 100
        piece = self.board[row][column]

        if piece.color==GREEN and (row,column,False) in self.validMoves:
            piece2 = self.moveturn

            self.board[row][column]=Figura(row,column,piece2.color)
            self.board[row][column].king = piece2.king
            self.board[piece2.row][piece2.column]=Figura(piece2.row,piece2.column,GREEN)
            fig=self.board[row][column]
            self.validMoves = []
            if fig.color==RED and row==0:
                fig.king=True
                self.board[row][column].king=True
            if fig.color==WHITE and row==7:
                fig.king=True
                self.board[row][column].king = True

            if self.turn==RED:
                self.turn=WHITE
            else:
                self.turn=RED
            return True
        if piece.color == GREEN and (row, column, True) in self.validMoves:
            piece2 = self.moveturn



            self.board[row][column] = Figura(row, column, piece2.color)
            self.board[row][column].king=piece2.king
            self.board[piece2.row][piece2.column] = Figura(piece2.row, piece2.column, GREEN)
            row1=(row+piece2.row)//2
            column1=(column+piece2.column)//2
            color = self.board[row1][column1].color
            self.board[row1][column1]=Figura(row1,column1,GREEN)
            fig = self.board[row][column]
            if color == RED:
                self.crvenef=self.crvenef-1
            else:
                self.belef=self.belef-1
            if fig.color==RED and row==0:
                fig.king=True
                self.board[row][column].king = True
            if fig.color==WHITE and row==7:
                fig.king=True
                self.board[row][column].king = True
            self.validMoves = []
            if self.turn==RED:
                self.turn=WHITE
            else:
                self.turn=RED
            return True
        return False
    def position(self,x,y,screen):
        piece = self.getPiece(x, y)
        if self.moveturn:
            blcon=self.move(x,y)
            if not blcon:
                self.moveturn=None
                self.validMoves = []
                self.position(x,y,screen)

        elif piece.color==self.turn:
            column = x // 100
            row = y // 100
            self.moveturn=self.board[row][column]
            self.getValidMoves(row,column)


    def getValidMoves(self,row,column):
        piece =self.board[row][column]
        color = piece.color

        if color == RED or piece.king:
            if (row-1)>=0 and (column-1)>=0:
                piece1=self.board[row-1][column-1]
                if piece1.color == GREEN:
                    self.validMoves.append((row - 1, column - 1,False))
                if (color == RED and piece1.color == WHITE and  (row-2)>=0 and (column-2)>=0) or (color==WHITE and piece1.color==RED and  (row-2)>=0 and (column-2)>=0):
                    piece11=self.board[row-2][column-2]
                    if piece11.color==GREEN:
                        self.validMoves.append((row - 2, column - 2,True))

            if (row-1)>=0 and (column+1)<8:
                piece2=self.board[row-1][column+1]
                if piece2.color == GREEN and (row - 1) >= 0 and (column + 1) < 8:
                    self.validMoves.append((row - 1, column + 1,False))
                if (color == RED and piece2.color == WHITE and (row - 2) >= 0 and (column + 2) < 8) or (color==WHITE and piece2.color==RED and (row - 2) >= 0 and (column + 2) < 8):
                    piece11 = self.board[row - 2][column + 2]
                    if piece11.color == GREEN:
                        self.validMoves.append((row - 2, column + 2, True))
        if color == WHITE or piece.king:
            if (row+1)<8 and (column-1)>=0:
                piece1=self.board[row+1][column-1]
                if piece1.color == GREEN:
                    self.validMoves.append((row + 1, column - 1,False))
                if (color == WHITE and piece1.color == RED and  (row+2)<8 and (column-2)>=0) or (color == RED and piece1.color==WHITE and  (row+2)<8 and (column-2)>=0):
                    piece11=self.board[row+2][column-2]
                    if piece11.color==GREEN:
                        self.validMoves.append((row + 2, column - 2,True))

            if (row+1)<8 and (column+1)<8:
                piece2=self.board[row+1][column+1]
                if piece2.color == GREEN and (row + 1) < 8 and (column + 1) < 8:
                    self.validMoves.append((row + 1, column + 1,False))
                if (color == WHITE and piece2.color == RED and (row + 2) < 8 and (column + 2) < 8) or (color == RED and piece2.color==WHITE and (row + 2) < 8 and (column + 2) < 8):
                    piece11 = self.board[row + 2][column + 2]
                    if piece11.color == GREEN:
                        self.validMoves.append((row + 2, column + 2, True))

