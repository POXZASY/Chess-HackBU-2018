import Chessboard
import location
import pygame
import Check
import capture
import threaten
import validMoves



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
        chessboard = Chessboard.makeChessboard()  # makes chessboard
        temp_pieces = Chessboard.list_of_pieces  # for saving state
        pieceselected = False
        turn = "WHITE"
        checkmate = False
        selected = []  # selected piece
        move_happened = False  # for *actually* making moves

        # MAIN LOOP
        while not checkmate:
            chessboard.updateChessboard(chessboard.dict_of_pieces.values(), self.screen)  # blits images
            if pieceselected == False:
                chessboard.list_of_pieces = Chessboard.dict_of_pieces.values
            else:
                temp_pieces = Chessboard.list_of_pieces

            if not move_happened:

                # SELECTING PIECE
                if pieceselected == False and pygame.mouse.get_pressed()[0] == True:
                    mousecoords = pygame.mouse.get_pos()
                    squarecoords = location.convertToNum(mousecoords)

                    for piece in temp_pieces:

                        if piece.x == squarecoords[0] and piece.y == squarecoords[1]:  # if the click is on a  piece
                            selected = piece  # TO REPLACE OF, USE selected.ID
                            pieceselected = True

                # MAKING MOVE
                if pieceselected == True and pygame.mouse.get_pressed()[0] == True:
                    valid_moves = validMoves.checkValidity(selected)  # LIST OF VALID MOVES#TODO
                    mousecoords = pygame.mouse.get_pos()
                    squarecoords = location.convertToNum(mousecoords)
                    if squarecoords in valid_moves:
                        selected.x = squarecoords[0]
                        selected.y = squarecoords[1]
                        capture.capture(selected)  # look for capture
                        pieceselected = False
                        selected = []
                    else:
                        pieceselected = False
                        selected = []
                    # LOOKING IF STILL IN CHECK AFTER 'MOVE'
                    for piece in temp_pieces:
                        if piece.team == turn and piece.type == "KING":
                            if Check.lookforCheck(piece):
                                move_happened = False
                            else:  # **ACTUALLY MOVES NOW**
                                move_happened = True
                                Chessboard.dict_of_pieces[selected.ID] = selected
                                Chessboard.list_of_pieces = temp_pieces

            elif move_happened:
                if turn == "WHITE":
                    turn = "BLACK"
                else:
                    turn = "WHITE"

        if checkmate:
            pass
            # display game over stuff here #TODO 


def main():
    play = Controller()
    play.mainloop()


main()
