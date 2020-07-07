from logica.fabricas import *
from logica.personaje import Personaje


class Director:

    def set_builder(self, builder):
        self.__builder = builder

    def get_personaje(self):
        personaje = Personaje()
        personaje.set_atributos(self.__builder.get_atributos())
        return personaje

class Builder:
    def get_atr(self):
        pass

class builder_ladron (Builder):
    def __init__(self):
        self.fabrica = fabrica_ladron()

    def get_atr(self):
        return self.fabrica.get_atributos()


class builder_perro_a (Builder):
    def __init__(self):
        self.fabrica = fabrica_perro_a()

    def get_atr(self):
        return self.fabrica.get_atributos()


class builder_perro_b (Builder):
    def __init__(self):
        self.fabrica = fabrica_perro_b()

    def get_atr(self):
        return self.fabrica.get_atributos()