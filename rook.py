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
        for i in range(len(moveList)):
            if team in allPiece[i][3]:
                del allPiece[i]
        for i in range(len(moveList)):
            #checks if piece color is same as possible move place (CAN'T MOVE BLACK ON BLACK) gets rid of same color squares
            if team in allPiece[i]["BLACK OR WHITE"]:
                del moveList[i]
        for i in range(len(moveList)):
            #checks if taken coordinate is in the movelist then deletes everything after
            if allPiece[i]["STRING OF CORDINATES"] is in moveList:
                del moveList[(i+1):]
        for i in range(8):
            if self.x + i > 8:
                del moveList[i]
            if self.x - i < 0:
                del moveList
            if self.y + i > 8:
                del moveList
            if self.y - i < 0:
                del moveList

    def movePiece(possibleMoves):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New Rook position
        """
