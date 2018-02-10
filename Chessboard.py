import pygame
import Square

class Chessboard(pygame.sprite.Sprite):

    def __init__(self, pieces):
        self.pieces = pieces  # lsit of piece objects
        self.squares = []  # list of squares represented as tuples of x,y,color
        self.squareObjs = []  # list of squares represented as objects
        self.all_squares = {}  # list of all pieces
        self.list_of_pieces = []
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

        r = 1  # row
        c = 1  # column
        # WHITE PIECES
        for i in range(17):
            team = "WHITE"
            if c > 8:
                c = 1
                r += 1
            if r == 2:
                piece = pawn.Pawn(c, r, team)
                self.list_of_pieces.append(piece)
                c += 1
                continue
            elif c == 1 or c == 8:
                piece = rook.Rook(c, r, team)
            elif c == 2 or c == 7:
                piece = knight.Knight(c, r, team)
            elif c == 3 or c == 6:
                piece = bishopBase.Bishop(c, r, team)
            elif c == 4:
                piece = queen.Queen(c, r, team)
            elif c == 5:
                piece = king.King(c, r, team)
            self.list_of_pieces.append(piece)
            c += 1
            
        r = 7
        c = 1
        # BLACK PIECES
        for i in range(17):
            team = "BLACK"
            if c > 8:
                c = 1
                r += 1
            if r == 7:
                piece = pawn.Pawn(c, r, team)
                self.list_of_pieces.append(piece)
                c += 1
                continue
            elif c == 1 or c == 8:
                piece = rook.Rook(c, r, team)
            elif c == 2 or c == 7:
                piece = knight.Knight(c, r, team)
            elif c == 3 or c == 6:
                piece = bishopBase.Bishop(c, r, team)
            elif c == 4:
                piece = queen.Queen(c, r, team)
            elif c == 5:
                piece = king.King(c, r, team)
            self.list_of_pieces.append(piece)
            c += 1

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
        self.all_squares = {i[0]: i[1] for i in templist}





