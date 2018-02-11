class King:
    def __init__(self, x, y, team, ID, KingFirstMove):
        self.x = x
        self.y = y
        self.team = team
        self.ID = ID
        self.imagefile = "assets/" + team + "king.png"
        self.image = pygame.image.load(self.imagefile)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def isFirstMove():
        if KingFirstMove == 0:
            KingFirstMove = 1 + KingFirstMove
            return True
        else:
            return False

    def validMoves(self, allPiece):
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

        if self.KingFirstMove:
            if [0, 6] and [0, 7] not in allPiece:
                moveList.append([7, 0])
            if [0, 2] and [0, 3] and [0, 4] not in allPiece:
                moveList.append([3, 0])

    def movePiece(possibleMoves):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
        if move[7, 0]:
        # castleRIght
        if move[3, 0]:
