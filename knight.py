class Knight:

    def __init__(self,x,y,team):
        self.x = x
        self.y = y
        self.team = team

    def validMoves(self,allPiece):
        """
        Checks vaild moves for knight
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        position = (self.x, self.y)
        allPiece = "things"
        moveList = []
        listofnew = [(self.x+2, self.y+1), (self.x+2, self.y-1),(self.x-2, self.y+1), (self.x-2, self.y-1),(self.x+1, self.y+2), (self.x+1, self.y-2), (self.x-1, self.y+2), (self.x-1, self.y-2)]
        for j in listofnew:
            for i in Chessboard.list_of_pieces:
                if j[0] == i.x and j[1]== i.y and self.team == i.team:
                    #do nothing
                else:
                    if 0<j[0]<9 and 0<j[1]< 9:
                        moveList.append(j[0],j[1])


    def movePiece(possibleMoves):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
