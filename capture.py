import pygame
import Chessboard


def capture(piece,list_of_pieces,chessboard):
    for i in chessboard.dict_of_pieces:
        if chessboard.dict_of_pieces[i].x == piece.x and chessboard.dict_of_pieces[i].y == piece.y:
            chessboard.dict_of_pieces.pop(i)
