import pygame

class Rook:

    def __init__(self,x,y,team, ID):
        self.x = x
        self.y = y
        self.team = team
        self.ID = ID
        self.imagefile = "assets/"+team+"rook.png"
        self.image = pygame.image.load(self.imagefile)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.num_moves = 0

    def validMoves(self,allPiece):
        """
        Checks vaild moves for rook
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        moveList = []
        for i in range(8) :
            moveList.append([self.x + i, self.y])
        for i in range(8):
            moveList.append([self.x - i, self.y])
        for i in range(8):
            moveList.append([self.x, self.y + i])
        for i in range(8):
            moveList.append([self.x, self.y - i])
        for piece in  allPiece:
            for i in range(len(moveList)):
                if self.team == piece.team:
                    moveList.remove(piece.x, piece.y)

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
        Outputs: New Rook position
        """
        self.x = move[0]
        self.y = move[1]
