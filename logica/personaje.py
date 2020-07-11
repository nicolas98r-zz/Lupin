import pygame
class Personaje:

    def set_atributos(self, atributos):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load(atributos[0])
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 200
        self.rect.centery = 250
        self.velocidad = atributos[1]

    def dibujar(self,superficie):
        superficie.blit(self.imagen, self.rect)