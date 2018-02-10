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

