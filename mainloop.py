import pygame
import Chessboard

class Controller:
    def __init__(self):
        pygame.init()
        self.width=800
        self.height=800
        self.screen = pygame.display.set_mode(self.width, self.height)
        self.sprites=pygame.sprite.Group() #all sprites
        self.whitepieces=pygame.sprite.Group()
        self.blackpieces=pygame.sprite.Group()

    def mainloop(self):
        Chessboard.makeChessboard()
        isRunning=True
        while isRunning:
            Chessboard.updateChessboard()



def main():

    play=Controller()
    play.mainloop()
main()