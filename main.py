import  pygame
from pygame import *
from logica import ladron, bloque

#Variables Globales
SCREEN_WITH = 300
SCREEN_HEIGHT = 240

pygame.init()
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))
pygame.display.set_caption("Lupin")
game_running = True
clock = pygame.time.Clock()

#Objetos
jugador = ladron.Ladron()
background = pygame.transform.scale(pygame.image.load("img/bg.png"), (400, 300))    

def crear_bloques():
    for i in range(0,300,30):
        obj_bloque = bloque.Bloque(i,0)
        obj_bloque.dibujar(screen)
    for i in range(0,3000,30):
        obj_bloque = bloque.Bloque(i,210)
        obj_bloque.dibujar(screen)
    for i in range(30,210,30):
        obj_bloque = bloque.Bloque(0,i)
        obj_bloque.dibujar(screen)
    for i in range(30,210,30):
        obj_bloque = bloque.Bloque(270,i)
        obj_bloque.dibujar(screen)

while game_running:
    clock.tick(25)

    screen.blit(background, (0, 0))

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
    
    crear_bloques()
    jugador.dibujar(screen)
    pygame.display.update()