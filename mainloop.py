import pygame
import Chessboard
import location


class Controller:
    def __init__(self):
        pygame.init()
        self.width=800
        self.height=800
        self.screen = pygame.display.set_mode(self.width, self.height)
        self.sprites=pygame.sprite.Group() #all sprites
        self.allpieces=pygame.sprite.Group()
        self.whitepieces=pygame.sprite.Group()
        self.blackpieces=pygame.sprite.Group()

    def mainloop(self):
        Chessboard.makeChessboard()
        pieceselected=False
        turn="WHITE"
        checkmate=False
        while checkmate==False:
            Chessboard.updateChessboard()
            if pieceselected==False and pygame.mouse.get_pressed()[0] == True:
                mousecoords=pygame.mouse.get_pos()
                squarecoords=location.convertToNum(mousecoords)
                if #identify if you clicked on a piece here
                    #IDENTIFY WHICH PIECE YOU CLICKED ON HERE
                    pieceselected=True
            if pieceselected==True and pygame.mouse.get_pressed()[0] == True:
                mousecoords = pygame.mouse.get_pos()
                squarecoords = location.convertToNum(mousecoords)
                if #confirm if valid move here
                    make valid move here
                    if turn == "WHITE":
                        turn == "BLACK"
                    else:
                        turn == "WHITE"
                    pieceselected==False
                    if they are in checkmate:
                        checkmate=True
                else:
                    pieceselected==False
        if checkmate==True:
            #display game over stuff here


def main():

    play=Controller()
    play.mainloop()
main()
