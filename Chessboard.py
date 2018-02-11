import pygame
import Square
import bishopBase
import king
import knight
import pawn
import pygame
import queen
import rook


class Chessboard:
    def __init__(self):
        self.pieces = []  # list of piece objects
        self.squares = []  # list of squares represented as tuples of x,y,color
        self.squareObjs = []  # list of squares represented as objects
        self.list_of_pieces = []
        self.dict_of_pieces = {}  # TO REFERENCE PIECES BASED ON  POSITION

    def makeChessboard(self):
        # Make Square Objects
        # column
        count = 1
        for y in range(1, 9):
            # row
            for x in range(1, 9):
                if count % 2 == 0:
                    color = "WHITE"
                else:
                    color = "BLACK"
                SSquare = [x, y, color]
                self.squares.append(SSquare)
                count += 1
                
        for i in range(len(self.squares)):

            temp_square = Square.Square(self.squares[i][0], self.squares[i][1], self.squares[i][2])  # make a square object
            self.squareObjs.append(temp_square)

        r = 1  # row
        c = 1  # column
        number = 1
        count = "Piece" + str(number)
        # WHITE PIECES
        for i in range(17):
            team = "WHITE"
            if c > 8:
                c = 1
                r += 1
            if r == 2:
                piece = pawn.Pawn(c, r, team, count)
                self.list_of_pieces.append(piece)
                self.dict_of_pieces[count] = piece
                number += 1
                c += 1
                continue
            elif c == 1 or c == 8:
                piece = rook.Rook(c, r, team, count)
            elif c == 2 or c == 7:
                piece = knight.Knight(c, r, team, count)
            elif c == 3 or c == 6:
                piece = bishopBase.Bishop(c, r, team, count)
            elif c == 4:
                piece = queen.Queen(c, r, team, count)
            elif c == 5:
                piece = king.King(c, r, team, count)
            self.list_of_pieces.append(piece)
            self.dict_of_pieces[count] = piece
            c += 1
            number += 1
        r = 7
        c = 1
        # BLACK PIECES
        number = 17
        count = "Piece" + str(number)
        for i in range(33):
            team = "BLACK"
            if c > 8:
                c = 1
                r += 1
            if r == 7:
                piece = pawn.Pawn(c, r, team, count)
                self.list_of_pieces.append(piece)
                self.dict_of_pieces[count] = piece
                number += 1
                c += 1
                continue
            elif c == 1 or c == 8:
                piece = rook.Rook(c, r, team, count)
            elif c == 2 or c == 7:
                piece = knight.Knight(c, r, team, count)
            elif c == 3 or c == 6:
                piece = bishopBase.Bishop(c, r, team, count)
            elif c == 4:
                piece = queen.Queen(c, r, team, count)
            elif c == 5:
                piece = king.King(c, r, team, count)
            self.list_of_pieces.append(piece)
            self.dict_of_pieces[count] = piece
            number += 1
            c += 1

    def updateChessboard(self, pieces, screen):
        """

        :param pieces: List of pieces currently in play
        :return: void
        """
        for square in self.squareObjs:
            square.update(pieces)
            screen.blit(square.surface, square.surface.get_rect())  # blit squares to screen

        for piece in pieces:
            screen.blit(piece.image, piece.image.get_rect())  # blit piece to pieces

        rows = 1
        columns = 1
        templist = []
        # for square in self.squareObjs:
        #     if columns > 8:
        #         columns = 1
        #         rows += 1
        #     templist += ((columns, rows), square)
        #     columns += 1
        # self.all_squares = {(i.x, i.y): i for i in templist}

        pygame.display.flip()
