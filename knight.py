import pygame


class Knight:

    def __init__(self,x,y,team,allPiece):
        self.x = x
        self.y = y
        self.team = team
        self.allPiece = allPiece
        self.type = "KNIGHT"
        self.imagefile = "assets/"+team+"Knight.png"
        self.image = pygame.image.load(self.imagefile)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.num_moves = 0

    def validMoves(self, allPiece):
        """
        Checks vaild moves for knight
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        moveList = []
        moveList.append([self.x + 2, self.y + 1])
        moveList.append([self.x - 2, self.y + 1])
        moveList.append([self.x + 2, self.y - 1])
        moveList.append([self.x - 2, self.y - 1])

        moveList.append([self.x + 1, self.y + 2])
        moveList.append([self.x - 1, self.y + 2])
        moveList.append([self.x + 1, self.y - 2])
        moveList.append([self.x - 1, self.y - 2])
        for piece in allPiece:
            if piece.team == self.team:
                moveList.remove([piece.x, piece.y])
        for i in range(8):
            if self.x + i > 8:
                del moveList[i]
            if self.x - i < 0:
                del moveList[i]
            if self.y + i > 8:
                del moveList[i]
            if self.y - i < 0:
                del moveList[i]
        return moveList

    def movePiece(possibleMoves):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
