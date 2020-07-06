import pygame

class Bloque (pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_bloque = pygame.image.load("img/Bloque.png")
        self.rect = self.imagen_bloque.get_rect()
        self.rect.x = pos_x
        self.rect.y= pos_y
        self.velocidad = 10

    def dibujar(self,superficie):
        superficie.blit(self.imagen_bloque, self.rect)