import Chessboard
import location
import pygame
import Check
import capture
import threaten
import sys


class Controller:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.sprites = pygame.sprite.Group()  # all sprites
        self.allpieces = pygame.sprite.Group()
        self.whitepieces = pygame.sprite.Group()
        self.blackpieces = pygame.sprite.Group()

    def mainloop(self):

        chessboard = Chessboard.Chessboard()
        chessboard.makeChessboard()  # makes chessboard
        chessboard.updateChessboard(chessboard.list_of_pieces, self.screen)
        temp_pieces = chessboard.list_of_pieces  # for saving state
        pieceselected = False
        turn = "WHITE"
        checkmate = False
        selected = []  # selected piece
        move_happened = False  # for *actually* making moves
        checkmate = False
        # MAIN LOOP
        while not checkmate:
            for event in pygame.event.get():
                print("Ok")
                checkmate = Check.inCheckmate
                chessboard.updateChessboard(chessboard.dict_of_pieces.values(), self.screen)  # blits images
                print("updates")
                if not pieceselected:
                    chessboard.list_of_pieces = chessboard.dict_of_pieces.values()
                else:
                    temp_pieces = Chessboard.list_of_pieces

                if not move_happened:
                    print("close")
                    # SELECTING PIECE
                    if not pieceselected and pygame.mouse.get_pressed()[0]:  # no piece selected, left click detected
                        print("Got here")
                        mousecoords = pygame.mouse.get_pos()
                        squarecoords = location.convertToNum(mousecoords)

                        for piece in temp_pieces:

                            if piece.x == squarecoords[0] and piece.y == squarecoords[1]:  # if the click is on a  piece
                                selected = piece  # TO REPLACE OF, USE selected.ID
                                pieceselected = True

                    # MAKING MOVE
                    if pieceselected and pygame.mouse.get_pressed()[0]:  # piece seleceted, left click detected
                        valid_moves = selected.validMoves(temp_pieces)
                        mousecoords = pygame.mouse.get_pos()
                        squarecoords = location.convertToNum(mousecoords)
                        if squarecoords in valid_moves:
                            selected.x = squarecoords[0]
                            selected.y = squarecoords[1]
                            capture.capture(selected)  # look for capture

                        # LOOKING IF STILL IN CHECK AFTER 'MOVE'
                        for piece in temp_pieces:
                            if piece.team == turn and piece.type == "KING":
                                if Check.lookforCheck(piece):
                                    move_happened = False
                                else:  # **ACTUALLY MOVES NOW**
                                    move_happened = True
                                    selected.num_moves +=1
                                    chessboard.dict_of_pieces[selected.ID] = selected
                                    chessboard.list_of_pieces = temp_pieces

                # CHANGE TEAM IF MOVE OCCURRED
                elif move_happened:
                    if turn == "WHITE":
                        turn = "BLACK"
                    else:
                        turn = "WHITE"
                    move_happened = False
                pieceselected = False
                selected = []


            # IGNORE
        while True:
            if checkmate:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

def main():
    play = Controller()
    play.mainloop()


main()
