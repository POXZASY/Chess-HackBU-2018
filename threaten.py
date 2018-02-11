import pygame
import Chessboard

def isThreatened(piece, list_of_pieces):
    for i in list_of_pieces:
        if (piece.x, piece.y) in i.validMoves():
            return True
    else:
        return False
def threats(piece, list_of_pieces): #returns threats to the piece
    threats=[]
    for i in list_of_pieces:
        if (piece.x, piece.y) in i.validMoves():
            threats=threats+i
    return threats