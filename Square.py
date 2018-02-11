import pygame
import location


class Square:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        if self.color == "BLACK":
            self.image = "assets/blackbox.png"
        else:
            self.image = "assets/whitebox.png"
        self.surface = pygame.image.load(self.image)
        #self.surface = pygame.Surface(location.convertToPixel([100, 100]))
        self.rect = self.surface.get_rect()
        self.rect.center = (x,y)
        self.hasPiece = False
    
    def update(self, pieces):
        for piece in pieces:
            if piece.x == self.x and piece.y == self.y:
                self.hasPiece = True
                return self.hasPiece
            else: 
                self.hasPiece = True
