import Chessboard
import location
import pygame

class Controller:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 800
        self.screen = pygame.display.set_mode(self.width, self.height)
        self.sprites = pygame.sprite.Group()  # all sprites
        self.allpieces = pygame.sprite.Group()
        self.whitepieces = pygame.sprite.Group()
        self.blackpieces = pygame.sprite.Group()

    def mainloop(self):
        Chessboard.makeChessboard()
        pieceselected = False
        turn = "WHITE"
        checkmate = False
        # MAIN LOOP
        while not checkmate:
            Chessboard.updateChessboard()
            temp_pieces = Chessboard.list_of_pieces
            if pieceselected == False and pygame.mouse.get_pressed()[0] == True:
                mousecoords = pygame.mouse.get_pos()
                squarecoords = location.convertToNum(mousecoords)
                for coords in Chessboard.getPieces(temp_pieces):
                    if  coords == squarecoords
                        # IDENTIFY WHICH PIECE YOU CLICKED ON HERE = piece
                        pieceselected = True
            if pieceselected == True and pygame.mouse.get_pressed()[0] == True:
                valid_moves = validMoves.checkValid()
                mousecoords = pygame.mouse.get_pos()
                squarecoords = location.convertToNum(mousecoords)
                if squarecoords in valid_moves:
                    #make valid move here
                    capture.capture(piece)
                    if turn == "WHITE":
                        turn = "BLACK"
                    else:
                        turn = "WHITE"
                    pieceselected = False
                    if they are in check:
                        checkmate = True
                else:
                    pieceselected = False
            for piece in Chessboard.list_of_pieces:
                if piece.team == turn and piece.type == "KING":
                    if Check.lookforCheck(piece):




        if checkmate:
            # display game over stuff here


def main():
    play = Controller()
    play.mainloop()


main()
