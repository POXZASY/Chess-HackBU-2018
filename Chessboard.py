import pygame
import Square

class Chessboard(pygame.sprite.Sprite):

    def __init__(self, pieces):
        self.pieces = pieces  # lsit of piece objects
        self.squares = []  # list of squares represented as tuples of x,y,color
        self.squareObjs = []  # list of squares represented as objects
        self.all_pieces = {}  # list of all pieces
        self.allpieces = 
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
                square = (x, y, color)
                self.squares.append(square)
                count += 1

        for square in self.squares:
            temp_square = Square.Square(square[0], square[1], [square[2]])  # make a square object
            self.squareObjs.append(temp_square)



    def updateChessboard(self, pieces, screen):
        """

        :param pieces: List of pieces currently in play
        :return: void
        """
        for square in self.squareObjs:
            screen.blit(square.surface, square.surface.getRect())  # blit squares to screen

        for piece in pieces:
            screen.blit(piece.surface, piece.getRect())  # blit piece to pieces

        rows = 1
        columns = 1
        templist = []
        for square in self.squareObjs:
            if columns > 8:
                columns = 1
                rows += 1
            templist += ((columns, rows), square)
            columns += 1
        self.all_pieces = {i[0]: i[1] for i in templist}





