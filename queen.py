import pygame


class Queen(pygame.sprite.Sprite):
    def __init__(self, x, y, team, ID):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.team = team
        self.PawnFirstMove = 0
        self.ID = ID
        self.type = "QUEEN"
        self.imagefile = "assets/" + team + "queen.png"
        self.image = pygame.image.load(self.imagefile)
        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def validMoves(self, list_of_pieces):
        """
        Checks vaild moves for pawn
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        movelist = []
        # Rook Movement
        xval = self.x - 1  # horizontal
        while xval != 0:
            for i in list_of_pieces:  # check if there's a piece there
                if i.x == xval and i.y == self.y:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((xval, self.y))
                        break
            movelist.append((xval, self.y))
            xval = xval - 1
        xval = self.x + 1
        while xval != 9:
            for i in list_of_pieces:  # check if there's a piece there
                if i.x == xval and i.y == self.y:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((xval, self.y))
                        break
            movelist.append((xval, self.y))
            xval = xval + 1
        yval = self.y - 1  # vertical
        while yval != 0:
            for i in list_of_pieces:  # check if there's a piece there
                if i.x == self.x and i.y == yval:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((self.x, yval))
                        break
            movelist.append((self.x, yval))
            yval = yval - 1
        yval = self.y + 1
        while yval != 9:
            for i in list_of_pieces:  # check if there's a piece there
                if i.x == self.x and i.y == yval:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((self.x, yval))
                        break
            movelist.append((self.x, yval))
            yval = yval + 1
        #Bishop Movement
        xval = self.x - 1
        yval = self.y - 1
        while xval != 0 and yval != 0:
            for i in list_of_pieces:  # check if there's a piece there
                if i.x == xval and i.y == yval:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((xval, yval))
                        break
            movelist.append((xval, yval))
            xval = xval - 1
            yval = yval - 1
        xval = self.x + 1
        yval = self.y + 1
        while xval != 9 and yval != 9:
            for i in list_of_pieces:  # check if there's a piece there
                if i.x == xval and i.y == yval:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((xval, yval))
                        break
            movelist.append((xval, yval))
            xval = xval + 1
            yval = yval + 1
        xval = self.x - 1
        yval = self.y + 1
        while xval != 0 and yval != 9:
            for i in list_of_pieces:  # check if there's a piece there
                if i.x == xval and i.y == yval:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((xval, yval))
                        break
            movelist.append((xval, yval))
            xval = xval - 1
            yval = yval + 1
        xval = self.x + 1
        yval = self.y - 1
        while xval != 0 and yval != 0:
            for i in list_of_pieces:  # check if there's a piece there
                if i.x == xval and i.y == yval:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((xval, yval))
                        break
            movelist.append((xval, yval))
            xval = xval + 1
            yval = yval - 1
        return movelist

    def movePiece(self, move):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
        self.x = move[0]
        self.y = move[1]
