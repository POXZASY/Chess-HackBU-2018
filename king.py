import pygame


class King(pygame.sprite.Sprite):
    def __init__(self, x, y, team, ID):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.team = team
        self.ID = ID
        self.type = "KING"
        self.imagefile = "assets/" + team + "king.png"
        self.image = pygame.image.load(self.imagefile)
        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.num_moves = 0

    def validMoves(self, allPiece):
        """
        Checks vaild moves for King
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """

        moveList = []
        moveList.append([self.x + 1, self.y + 1])
        moveList.append([self.x + 1, self.y])
        moveList.append([self.x - 1, self.y])
        moveList.append([self.x + 1, self.y - 1])
        moveList.append([self.x, self.y + 1])
        moveList.append([self.x, self.y - 1])
        moveList.append([self.x - 1, self.y + 1])
        moveList.append([self.x - 1, self.y - 1])

        for i in moveList:
            if self.x + 1 > 8 or self.y + 1 > 8 or self.x - 1 < 0 or self.y - 1 > 8:
                moveList.remove(i)
        team_coords = []
        for piece in allPiece:
            if piece.team == self.team:
                if [piece.x, piece.y] in moveList:
                    moveList.remove([piece.x, piece.y])
                team_coords += [piece.x, piece.y]  # for castling

        if self.num_moves == 0:
            if self.team == "WHITE":
                if [2, 1] and [3, 1] and [4,1] not in team_coords:
                    moveList.append([3, 1])
                if [6, 1] and [7, 1] not in team_coords:
                    moveList.append([3, 0])
            if self.team == "WHITE":
                if [2, 8] and [3, 8] and [4,8] not in team_coords:
                    moveList.append([3, 8])
                if [6, 8] and [7, 8] not in team_coords:
                    moveList.append([3, 8])
        return moveList

    def didCastle(self):
        """
        returns t/f if king just tried to castle
        :return:
        """
        castling_pos = [(3, 1), (7, 1), (3, 8), (7, 8)]
        if self.num_moves == 0 and (self.x, self.y) in castling_pos:
            return True
        else:
            return False
    def movePiece(self, move):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
        self.x = move[0]
        self.y = move[1]
