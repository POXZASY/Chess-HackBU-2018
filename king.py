class King:

    def __init__(self,x,y,team):
        self.x = x
        self.y = y
        self.team = team

    def validMoves(self,allPiece):
        """
        Checks vaild moves for King
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        postion = (self.x, self.y)
        allPiece = "things"
        moveList = []
        moveList.append([self.x + 1, self.y + 1])
        moveList.append([self.x + 1, self.y])
        moveList.append([self.x - 1, self.y])
        moveList.append([self.x + 1, self.y - 1])
        moveList.append([self.x, self.y + 1])
        moveList.append([self.x, self.y - 1])
        moveList.append([self.x - 1, self.y + 1])
        moveList.append([self.x - 1, self.y - 1])

        if self.x + 1 > 8 or self.y + 1 > 8 or self.x - 1 < 0 or self.y - 1 > 8:
            del moveList[i]

    def movePiece(possibleMoves):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
