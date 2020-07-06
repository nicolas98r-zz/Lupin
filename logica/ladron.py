import pygame

class Ladron (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_ladron = pygame.image.load("img/Ladron.png")
        self.rect = self.imagen_ladron.get_rect()
        self.rect.x = 150
        self.rect.y= 100
        self.velocidad = 10

    def dibujar(self,superficie):
        superficie.blit(self.imagen_ladron, self.rect)
