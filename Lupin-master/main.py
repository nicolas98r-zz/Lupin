from pygame import *
from logica.constructores import *
from logica.fabricas import *

#Variables Globales
SCREEN_WITH = 400
SCREEN_HEIGHT = 300

pygame.init()
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))
pygame.display.set_caption("Lupin")
game_running = True
clock = pygame.time.Clock()
director = Director()
director.set_builder(fabrica_perro_b())
jugador = director.get_personaje()

background = pygame.transform.scale(pygame.image.load("img/bg.png"), (400, 300))

while game_running:
    clock.tick(25)

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key ==K_LEFT:
                jugador.rect.centerx -= jugador.velocidad
            if event.key ==K_RIGHT:
                jugador.rect.centerx += jugador.velocidad
            if event.key ==K_UP:
                jugador.rect.centery -= jugador.velocidad
            if event.key ==K_DOWN:
                jugador.rect.centery += jugador.velocidad
    
    jugador.dibujar(screen)
    pygame.display.update()