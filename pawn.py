class Pawn:

    def __init__(self,x,y,team, ID, PawnFirstMove):
        self.x = x
        self.y = y
        self.team = team
        self.PawnFirstMove = 0
        self.ID = ID

    def isFirstMove():
        if PawnFirstMove == 0:
            PawnFirstMove = 1 + PawnFirstMove
            return True
        else:
            return False

    def validMoves(self,allPiece):
        """
        Checks vaild moves for pawn
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        allPiece = "things"
        moveList = [[self.x, self.y+1]]
        if self.PawnFirstMove:
            moveList.append([self.x, self.y + 2])
        if allPiece[Corrodinates and color] == [self.x+1, self.y+1]:
            moveList.append([self.x + 1, self.y + 1])
        if allPiece[Corrodinates and color] == [self.x-1, self.y+1]:
            moveList.append([self.x-1, self.y + 1])
        for i in range(len(moveList)):
            #checks if piece color is same as possible move place (CAN'T MOVE BLACK ON BLACK) gets rid of same color squares
            if team is in allPiece[i]["BLACK OR WHITE"]:
                del moveList[i]
        for i in range(len(moveList))
            if [self.x, self.y+1] is in allPiece:
                del [self.x, self.y+1] in moveList
    def movePiece(possibleMoves):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
        """MOVE PIECE"""
        #After moved
        if self.y = 8:
            #replace Pawn(wait for key press)
