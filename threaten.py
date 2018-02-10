import pygame
import Chessboard

def isThreatened(piece):
    for i in Chessboard.list_of_pieces:
        if (piece.x, piece.y) in i.validMoves():
            return True
    else:
        return False