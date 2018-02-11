import pygame


class Pawn:

    def __init__(self, x, y, team, ID):
        self.x = x
        self.y = y
        self.team = team
        self.PawnFirstMove = 0
        self.ID = ID
        self.type = "PAWN"
        self.imagefile = "assets/" + team + "pawn.png"
        self.image = pygame.image.load(self.imagefile)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.num_moves = 0

    def validMoves(self, allPiece):  # TODO
        """
        Checks vaild moves for pawn
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        moveList = [(self.x, self.y + 1)]
        if self.num_moves == 0:
            moveList.append((self.x, self.y + 2))
        for piece in allPiece:
            if piece != self:
                if [piece.x, piece.y] == [self.x + 1, self.y + 1] and piece.team != self.team:
                    moveList.append([self.x + 1, self.y + 1])
                if [piece.x, piece.y] == [self.x - 1, self.y + 1] and piece.team != self.team:
                    moveList.append([self.x - 1, self.y + 1])
                if piece.team == self.team:
                    if [piece.x, piece.y] in moveList:
                        moveList.remove([piece.x, piece.y])
                for i in range(len(moveList)):
                    if [self.x, self.y + 1] == [piece.x, piece.y]:
                        moveList.remove([self.x, self.y + 1])
        return moveList

    def movePiece(self, move):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
        """MOVE PIECE"""
        # After moved
        self.x = move[0]
        self.y = move[1]
