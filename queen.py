import pygame


class Queen:
    def __init__(self, x, y, team, ID):
        self.x = x
        self.y = y
        self.team = team
        self.PawnFirstMove = 0
        self.ID = ID
        self.imagefile = "assets/" + team + "queen.png"
        self.image = pygame.image.load(self.imagefile)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def validMoves(self, allPiece):
        """
        Checks vaild moves for pawn
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        moveList = []
        # Rook Movement
        for i in range(8):
            moveList.append([self.x + i, self.y])
        for i in range(8):
            moveList.append([self.x - i, self.y])
        for i in range(8):
            moveList.append([self.x, self.y + i])
        for i in range(8):
            moveList.append([self.x, self.y - i])
        # Bishop Movement
        for i in range(8):
            moveList.append([self.x + i, self.y + i])
        for i in range(8):
            moveList.append([self.x + i, self.y - i])
        for i in range(8):
            moveList.append([self.x - i, self.y + i])
        for i in range(8):
            moveList.append([self.x - i, self.y - i])
        for piece in allPiece:
            for i in range(len(moveList)):
                # checks if piece color is same as possible move place (CAN'T MOVE BLACK ON BLACK) gets rid of same color squares
                if self.team == piece.team:
                    del moveList[i]
            for i in range(len(moveList)):
                # checks if taken coordinate is in the move list then deletes everything after
                if [piece.x, piece.y]:
                    moveList.remove([i + 1])
            for i in range(8):
                if self.x + i > 8:
                    del moveList[i]
                if self.x - i < 0:
                    del moveList[i]
                if self.y + i > 8:
                    del moveList[i]
                if self.y - i < 0:
                    del moveList[i]

    def movePiece(self, move):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
        self.x = move[0]
        self.y = move[1]
