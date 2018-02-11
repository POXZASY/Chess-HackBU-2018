import pygame
import location


class Square():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        if color == "Black":
            rgb = (0, 0, 0)
        else:
            rgb = (255, 255, 255)
        self.surface = pygame.Surface(location.convertToPixel([x, y]))
        self.surface.fill(rgb)
        self.hasPiece = False
    
    def update(self, pieces):
        for piece in pieces:
            if piece.x == self.x and piece.y == self.y:
                self.hasPiece = True
                return self.hasPiece
            else: 
                self.hasPiece = True
