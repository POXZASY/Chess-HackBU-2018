import pygame
import Chessboard

def capture(piece,list_of_pieces):
    for i in list_of_pieces:
        if i.x == piece.x and i.y == piece.y:
            #Delete i forever