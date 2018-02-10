import pygame
import location


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        if color == "Black":
            rgb = (0, 0, 0)
        else:
            rgb = (255, 255, 255)
        self.surface = pygame.Surface((location.convertToPixel(x), location.convertToPixel(y)))
        self.surface.fill(rgb)

    def hasPiece(self, pieces):
        for piece in pieces:
            if piece.x == self.x and piece.y == self.y:
                return True
