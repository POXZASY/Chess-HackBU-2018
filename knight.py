class Knight:
    def __init__(self, x, y, team, ID):
        self.x = x
        self.y = y
        self.team = team
        self.ID = ID
        self.imagefile = "assets/" + team + "knight.png"
        self.image = pygame.image.load(self.imagefile)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def validMoves(self, list_of_pieces):
        """
        Checks vaild moves for knight
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        movelist = []
        listofnew = [(self.x + 2, self.y + 1), (self.x + 2, self.y - 1), (self.x - 2, self.y + 1),
                     (self.x - 2, self.y - 1), (self.x + 1, self.y + 2), (self.x + 1, self.y - 2),
                     (self.x - 1, self.y + 2), (self.x - 1, self.y - 2)]
        for j in listofnew:
            for i in list_of_pieces:
                if j[0] == i.x and j[1] == i.y and self.team == i.team:
                # do nothing
                else:
                    if 0 < j[0] < 9 and 0 < j[1] < 9:
                        movelist.append(j[0], j[1])
        return movelist
