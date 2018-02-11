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
        self.KingFirstMove = KingFirstMove

    def isFirstMove(self):
        if self.KingFirstMove:
            KingFirstMove = False
            return True
        else:
            return False

    def validMoves(self, allPiece):
        """
        Checks vaild moves for King
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """

        moveList = []
        moveList.append([self.x + 1, self.y + 1])
        moveList.append([self.x + 1, self.y])
        moveList.append([self.x - 1, self.y])
        moveList.append([self.x + 1, self.y - 1])
        moveList.append([self.x, self.y + 1])
        moveList.append([self.x, self.y - 1])
        moveList.append([self.x - 1, self.y + 1])
        moveList.append([self.x - 1, self.y - 1])

        for i in moveList:
            if self.x + 1 > 8 or self.y + 1 > 8 or self.x - 1 < 0 or self.y - 1 > 8:
                moveList.remove(i)

        if self.isFirstMove:
            if [0, 6] and [0, 7] not in allPiece:
                moveList.append([7, 0])
            if [0, 2] and [0, 3] and [0, 4] not in allPiece:
                moveList.append([3, 0])

    def movePiece(self, move):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
        self.x = move[0]
        self.y = move[1]
