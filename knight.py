class Knight:

    def __init__(self,x,y,team,allPiece):
        self.x = x
        self.y = y
        self.team = team
        self.allPiece = allPiece

    def validMoves(self,allPiece):
        """
        Checks vaild moves for knight
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        postion = (self.x, self.y)
        allPiece = "things"
        moveList = []
        moveList.append([self.x + 2, self.y + 1])
        moveList.append([self.x - 2, self.y + 1])
        moveList.append([self.x + 2, self.y - 1])
        moveList.append([self.x - 2, self.y - 1])

        moveList.append([self.x + 1, self.y + 2])
        moveList.append([self.x - 1, self.y + 2])
        moveList.append([self.x + 1, self.y - 2])
        moveList.append([self.x - 1, self.y - 2])
        for i in range(len(moveList)):
            if team is in allPiece[i][3]:
                del allPiece[i]
        for i in range(len(moveList)):
            #checks if piece color is same as possible move place (CAN'T MOVE BLACK ON BLACK) gets rid of same color squares
            if team is in allPiece[i]["BLACK OR WHITE"]:
                del moveList[i]

    def movePiece(possibleMoves):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
