class Bishop:

    def __init__(self,x,y,team):
        self.x = x
        self.y = y
        self.team = team

    def validMoves(self,allPiece):
        """
        Checks vaild moves for bishop
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        postion = (self.x, self.y)
        allPiece = things
        moveList = []
        for i in range(8):
            moveList.append([self.x + i, self.y + i])
        for i in range(8):
            moveList.append([self.x + i, self.y - i])
        for i in range(8):
            moveList.append([self.x - i, self.y + i])
        for i in range(8):
            moveList.append([self.x - i, self.y - i])
        for i in range(len(moveList)):
            if team is in allPiece[i][3]:
                del allPiece[i]


    def movePiece(possibleMoves):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New rook position
        """
