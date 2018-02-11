import pygame

class Rook(pygame.sprite.Sprite):

    def __init__(self,x,y,team, ID):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.team = team
        self.type = "ROOK"
        self.ID = ID
        self.imagefile = "assets/"+team+"rook.png"
        self.image = pygame.image.load(self.imagefile)
        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.num_moves = 0

    def validMoves(self,list_of_pieces):
        """
        Checks vaild moves for rook
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        movelist=[]
        xval=self.x-1 #horizontal
        while xval != 0:
            for i in list_of_pieces: #check if there's a piece there
                if i.x == xval and i.y == self.y:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((xval, self.y))
                        break
            movelist.append((xval, self.y))
            xval=xval-1
        xval=self.x+1
        while xval != 9:
            for i in list_of_pieces: #check if there's a piece there
                if i.x == xval and i.y == self.y:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((xval, self.y))
                        break
            movelist.append((xval, self.y))
            xval=xval+1
        yval=self.y-1 #vertical
        while yval != 0:
            for i in list_of_pieces: #check if there's a piece there
                if i.x == self.x and i.y == yval:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((self.x, yval))
                        break
            movelist.append((self.x, yval))
            yval=yval-1
        yval=self.y+1
        while yval != 9:
            for i in list_of_pieces: #check if there's a piece there
                if i.x == self.x and i.y == yval:
                    if i.team == self.team:
                        break
                    else:
                        movelist.append((self.x, yval))
                        break
            movelist.append((self.x, yval))
            yval=yval+1
        return movelist
    def movePiece(self, move):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New Rook position
        """
        self.x = move[0]
        self.y = move[1]
