import pygame

class Rook:

    def __init__(self,x,y,team, ID):
        self.x = x
        self.y = y
        self.team = team
        self.type = "ROOK"
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
        for piece in allPiece:
            for i in range(len(moveList)):
                if self.team == piece.team:
                    if [piece.x, piece.y] in moveList:
                        moveList.remove([piece.x, piece.y])

            for i in range(len(moveList)):
                # checks if taken coordinate is in the move list then deletes everything after
                if [piece.x, piece.y] in moveList:
                    del moveList[i:]
            for i in range(8):
                if self.x + i > 8:
                    for move in moveList:
                        if move[0] == self.x+i:
                            del move
                if self.x - i < 0:
                    for move in moveList:
                        if move[0] == self.x-i:
                            del move
                if self.y + i > 8:
                    for move in moveList:
                        if move[0] == self.y+i:
                            del move
                if self.y - i < 0:
                    for move in moveList:
                        if move[0] == self.y-i:
                            del move
        return moveList
    def movePiece(self, move):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New Rook position
        """
        self.x = move[0]
        self.y = move[1]
