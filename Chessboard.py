import pygame


class Chessboard(pygame.sprite.Sprite):

    def __init__(self, pieces):
        self.pieces = pieces
        self.squares = []
        self.squareObjs = []

    def makeChessboard(self):
        for x in range(1,9):
            count = 1
            # columns
            for y in range(1, 9):
                if count%2 == 1:
                    color = "White"
                else:
                    color = "Black"
                square = (x,y,color)
                self.squares.append(square)
        for square in self.squares:
            square = Square.makeSquares
            self.squareObjs.append(square)

    def updateChessboard(self, pieces):
        """
        Calls Make Square and blits everything
        :param pieces: List of pieces currently in play
        :return: void
        """
        # Make Square Objects
        # rows



