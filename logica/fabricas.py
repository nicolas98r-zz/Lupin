import pygame
from logica.personaje import Personaje


class Fabrica:
    def __init__(self):
        pass

    def get_atributos(self):
        pass

class fabrica_ladron(pygame.sprite.Sprite, Fabrica):
    def __init__(self):
        self.atributos = ("img/Ladron.png", 10)

    def get_atributos(self):
        return self.atributos

class fabrica_perro_a(pygame.sprite.Sprite, Fabrica):
    def __init__(self):
        self.atributos = "img/PerroA.png", 10

    def get_atributos(self):
        return self.atributos

class fabrica_perro_b(pygame.sprite.Sprite, Fabrica):
    def __init__(self):
        self.atributos = "img/PerroB.png", 12

    def get_atributos(self):
        return self.atributos