import pygame


class Pawn(pygame.sprite.Sprite):

    def __init__(self, x, y, team, ID):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.team = team
        self.PawnFirstMove = 0
        self.ID = ID
        self.imagefile = "assets/" + team + "pawn.png"
        self.image = pygame.image.load(self.imagefile)
        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.num_moves = 0
        self.type = type

    def validMoves(self, list_of_pieces):  # TODO
        """
        Checks vaild moves for pawn
        Inputs: allPiece
        Outputs: Array of arrays of possible positions (possibleMoves)
        """
        movelist = []
        for i in list_of_pieces: #move one up
            if self.team == "WHITE":
                if i.x==self.x and i.y==self.y+1:
                    break
                movelist.append((self.x, self.y + 1))
            else:
                if i.x==self.x and i.y==self.y-1:
                    break
                movelist.append((self.x, self.y - 1))
        if self.num_moves == 0: #move two up
            for i in list_of_pieces:
                if self.team == "WHITE":
                    if i.x == self.x and i.y == self.y + 2:
                        break
                    elif i.x == self.x and i.y == self.y + 1:
                        break
                    movelist.append((self.x, self.y + 2))
                else:
                    if i.x == self.x and i.y == self.y - 2:
                        break
                    elif i.x == self.x and i.y == self.y - 1:
                        break
                    movelist.append((self.x, self.y - 2))
        for i in list_of_pieces: #capture
            if self.team == "WHITE":
                if i.x==self.x+1 and abs(self.y-i.y)==1 and i.team=="BLACK":
                    movelist.append((i.x, i.y))
            else:
                if i.x==self.x-1 and abs(self.y-i.y)==1 and i.team=="WHITE":
                    movelist.append((i.x, i.y))



        #en passant
        for piece in list_of_pieces:
            if self.y==piece.y and abs(self.x-piece.x)==1 and piece.type=="PAWN" and piece.num_moves==0:
                if piece.team == "WHITE":
                    movelist.append((piece.x, piece.y-1))
                else:
                    movelist.append((piece.x, piece.y+1))
        return movelist

    def movePiece(self, move):
        """
        MovesPiece to vaid space
        Inputs: possibleMoves
        Outputs: New pawn position
        """
        """MOVE PIECE"""
        # After moved
        self.x = move[0]
        self.y = move[1]
