import pygame
import Chessboard

def isThreatened(cPiece, list_of_pieces):
    for piece in list_of_pieces:
        if [piece.x, piece.y] in cPiece.validMoves(list_of_pieces):
            return True
    else:
        return False

def threats(cPiece,list_of_pieces): #returns threats to the piece
    threats=[]
    for piece in list_of_pieces:
        if (piece.x, piece.y) in cPiece.validMoves(list_of_pieces):
            threats.append(piece)
    return threats
