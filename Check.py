import pygame
import threaten
import Chessboard

def inCheck(turn):
    for i in Chessboard.list_of_pieces:
        if i.team == turn and i.type == "KING" and threaten.isThreatened(i)==True:
            return True
    else:
        return False

