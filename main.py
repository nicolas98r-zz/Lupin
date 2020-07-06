import  pygame
from pygame import *
from logica import ladron, bloque

#Variables Globales
SCREEN_WITH = 510
SCREEN_HEIGHT = 270
mapa = [
    "XXXXXXXXXXXXXXXXX",
    "X      XXX      X",
    "X      XXX      X",
    "X      XXX      X",
    "X               X",
    "X  XX  XXX      X",
    "X      XXX      X",
    "X      XXX      X",
    "XXXXXXXXXXXXXXXXX"
    ]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))
pygame.display.set_caption("Lupin")
game_running = True
clock = pygame.time.Clock()

#Objetos
jugador = ladron.Ladron()
lista_bloques = []
background = pygame.transform.scale(pygame.image.load("img/bg.png"), (SCREEN_WITH, SCREEN_HEIGHT))    

def dibujar_bloques(superficie, mapa):
    x = 0
    y = 0
    for fila in mapa:
        for i in fila:
            if i == "X":
                obj_bloque = bloque.Bloque(x, y)
                lista_bloques.append(obj_bloque)
                obj_bloque.dibujar(superficie)
            x +=30
        x = 0
        y += 30

while game_running:
    clock.tick(25)

    screen.blit(background, (0, 0))

    jugador.dibujar(screen)
    dibujar_bloques(screen, mapa)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key ==K_LEFT:
                jugador.rect.x -= jugador.velocidad
            if event.key ==K_RIGHT:
                jugador.rect.x += jugador.velocidad
            if event.key ==K_UP:
                jugador.rect.y -= jugador.velocidad
            if event.key ==K_DOWN:
                jugador.rect.y += jugador.velocidad
    for i in lista_bloques:
        if jugador.rect.colliderect(i):
            jugador.rect.x -=jugador.velocidad
            jugador.rect.y -= jugador.velocidad    
    
    pygame.display.update()