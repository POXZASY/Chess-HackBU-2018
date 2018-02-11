# import pygame
# import location
#
#
# class Square(pygame.sprite.Sprite):
#     def __init__(self, x, y, color):
#         pygame.sprite.Sprite.__init__(self)
#         self.x = x
#         self.y = y
#         self.colorsq = color
#         if self.colorsq == "BLACK":
#             self.imagefile = "assets/blackbox.png"
#         else:
#             self.imagefile = "assets/whitebox.png"
#         self.image = pygame.image.load(self.imagefile)
#         #self.surface = pygame.Surface(location.convertToPixel([100, 100]))
#         self.rect = self.image.get_rect()
#         self.rect.center = (x,y)
#         self.hasPiece = False
#
#     def update(self, pieces):
#         for piece in pieces:
#             if piece.x == self.x and piece.y == self.y:
#                 self.hasPiece = True
#                 return self.hasPiece
#             else:
#                 self.hasPiece = True
