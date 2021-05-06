import pygame
from tabla import Tabla
import copy

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
size = (800, 800)
DEPTH = 4


def minmax(depth, tabla):
    maxList = []
    moveval = []
    if (tabla.crvenef == 0):
        return 100
    if (tabla.belef == 0):
        return -100

    if (depth == 0):
        return tabla.belef - tabla.crvenef

    for row in range(8):
        for column in range(8):
            if tabla.turn == tabla.board[row][column].color:
                tabla.getValidMoves(row, column)
                for i in tabla.validMoves:

                    (row1, column1, truth) = i
                    tabla1 = copy.deepcopy(tabla)
                    tabla1.moveturn = tabla.board[row][column]
                    tabla1.move(column1 * 101, row1 * 101)
                    depth1 = depth - 1
                    k = minmax(depth1, tabla1)
                    maxList.append(k)
                    if depth == DEPTH:
                        moveval.append(((row, column), (row1, column1), k))

                tabla.validMoves = []
    if maxList == [] and tabla.turn == RED:
        return 100
    if maxList == [] and tabla.turn == WHITE:
        return -100
    if (tabla.turn == RED):

        max1 = min(maxList)
    else:
        max1 = max(maxList)

    if depth == DEPTH:
        for j in moveval:

            ((row, column), (row1, column1), k) = j

            if k == max1:
                tabla.moveturn = tabla.board[row][column]
                tabla.getValidMoves(row, column)
                tabla.move(column1 * 101, row1 * 101)
                return 1

    return max1