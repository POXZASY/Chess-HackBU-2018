import pygame
import Square

class Chessboard(pygame.sprite.Sprite):

    def __init__(self, pieces):
        self.pieces = pieces
        self.squares = []
        self.squareObjs = []

    def makeChessboard(self):
        # Make Square Objects
        # column
        count = 1
        for y in range(1,9):

            # row
            for x in range(1, 9):
                if count%2 == 0:
                    color = "White"
                else:
                    color = "Black"
                square = (x,y,color)
                self.squares.append(square)
                count+=1

        for square in self.squares:
            tempSquare = Square(square[0], square[1], [square[2]])
            self.squareObjs.append(tempSquare)

    def updateChessboard(self, pieces, screen):
        """

        :param pieces: List of pieces currently in play
        :return: void
        """
        for square in self.squareObjs:








