class Bishop:
    def __init__(self, x, y, team, ID):
        self.x = x
        self.y = y
        self.team = team
        self.ID = ID
        self.imagefile = "assets/" + team + "bishop.png"
        self.image = pygame.image.load(self.imagefile)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def validMoves(self, allPiece):
        """
        Checks vaild moves for bishop
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
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
            # checks if piece color is same as possible move place (CAN'T MOVE BLACK ON BLACK) gets rid of same color squares
            if team is in allPiece[i]["BLACK OR WHITE"]:
                del moveList[i]
        for i in range(len(moveList)):
            # checks if taken coordinate is in the movelist then deletes everything after
            if allPiece[i]["STRING OF CORDINATES"] in moveList:
                del moveList[(i + 1):]
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
        Outputs: New rook position
        """
