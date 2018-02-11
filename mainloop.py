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
        temp_pieces = Chessboard.list_of_pieces  # for saving state
        all_pieces = Chessboard.list_of_pieces
        pieceselected = False
        turn = "WHITE"
        checkmate = False
        selected = null  # selected piece
        move_happened = False  # for making moves
        # MAIN LOOP
        while not checkmate:
            Chessboard.updateChessboard(all_pieces, self.screen)
            if pieceselected == false:
                all_pieces = Chessboard.list_of_pieces  # for saving state
            else:
                temp_pieces = all_pieces
            if not move_happened:
                #SELECTING PIECE
                if pieceselected == False and pygame.mouse.get_pressed()[0] == True:
                    mousecoords = pygame.mouse.get_pos()
                    squarecoords = location.convertToNum(mousecoords)
                    for piece in temp_pieces:
                        if piece.x == squarecoords[0] and piece.y == squarecoords[1]:  # if the click is ona  piece
                            selected = piece
                            pieceselected = True
                #MAKING MOVE
                if pieceselected == True and pygame.mouse.get_pressed()[0] == True:
                    valid_moves = validMoves.checkValidity(selected)  # LIST OF VALID MOVES*************
                    mousecoords = pygame.mouse.get_pos()
                    squarecoords = location.convertToNum(mousecoords)
                    if squarecoords in valid_moves:
                        selected.x = squarecoords[0]
                        selected.y = squarecoords[1]
                        capture.capture(selected)  # look for capture
                        pieceselected = False
                        selected = null
                        if they are in check:
                            checkmate = True
                    else:
                        pieceselected = False
                        selected = null

                for piece in temp_pieces:
                    if piece.team == turn and piece.type == "KING":
                        if Check.lookforCheck(piece):
                            move_happened = false
                        else:
                            move_happened = true
            elif move_happened:
                if turn == "WHITE":
                    turn = "BLACK"
                else:
                    turn = "WHITE"





        if checkmate:
            # display game over stuff here


def main():
    play = Controller()
    play.mainloop()


main()
