""" 
 Mostramos como usar un sprite respaldado por un gráfico.
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Vídeo explicativo: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
 
# Definimos algunos colores
NEGRO = (0, 0 ,0)
ROJO= (255, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERDEROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
AMARILLO = (255,240,0)
  
pygame.init()
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
  
#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
 
hecho = False
 
  
# Se usa para establecer cuan rápido se actualiza la pantalla
 
reloj = pygame.time.Clock()

movix=20
moviy=20
direccion="abajo"
  
# -------- Bucle principal del Programa -----------
while not hecho: #While hecho == False: o defininrlo While hecho != True: 
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        
    
    
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
  
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
     
    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    
    
    #creo un rectangolo en la plantalla
    if moviy<400 and direccion=="abajo":
        pantalla.fill(VERDE)
        pygame.draw.ellipse(pantalla, ROJO, [movix, moviy, 100, 100])
        pygame.draw.rect(pantalla, ROJO, [movix+100, moviy+10, 100, 100])
        pygame.draw.ellipse(pantalla, ROJO, [movix+200, moviy+20, 100, 100])
        pygame.draw.rect(pantalla, ROJO, [movix+300, moviy+30, 100, 100])
        pygame.draw.ellipse(pantalla, ROJO, [movix+400, moviy+50, 100, 100])
        moviy=moviy+10
    if moviy>=400:
        direccion="arriba"
    if moviy>0 and direccion=="arriba":
        pantalla.fill(ROJO)
        pygame.draw.rect(pantalla, VERDE, [movix, moviy+50, 100, 100])
        pygame.draw.ellipse(pantalla, VERDE, [movix+100, moviy+30, 100, 100])
        pygame.draw.rect(pantalla, VERDE, [movix+200, moviy+20, 100, 100])
        pygame.draw.ellipse(pantalla, VERDE, [movix+300, moviy+10, 100, 100])
        pygame.draw.rect(pantalla, VERDE, [movix+400, moviy, 100, 100])
        moviy=moviy-10
    if moviy<=0:
        direccion="abajo"
        
    #movix=movix+10
    
    
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)
     
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()