import pygame


class Bishop(pygame.sprite.Sprite):
    def __init__(self, x, y, team, ID):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.team = team
        self.ID = ID
        self.type = "BISHOP"
        self.imagefile = "assets/" + team + "bishop.png"
        self.image = pygame.image.load(self.imagefile)
        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.num_moves = 0

    def validMoves(self, allPiece):
        """
        Checks vaild moves for bishop
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """

        movelist = []
        xval = self.x - 1
        yval = self.y - 1
        while xval != 0 and yval!=0:
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
        Outputs: New rook position
        """
        self.x = move[0]
        self.y = move[1]
