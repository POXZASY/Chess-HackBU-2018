import pygame
import Chessboard

def capture(piece):
    for i in Chessboard.list_of_pieces:
        if i.x == piece.x and i.y == piece.y:
            #Delete i forever