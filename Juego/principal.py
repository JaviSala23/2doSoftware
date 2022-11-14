
 #zona de importacion de recusos como librerias y clase
import pygame
from lib.elementos import Jugador , Escenario #importamos la clase que queremos usar de la carpeta lib, del archivo elemento
 
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

#  --------------------Espacio para generar los objetos--------------------

#generamos el objeto jugador ------------------------------------------------

jugador1=Jugador()
imagenNave=pygame.image.load('Juego/recursos/Nave.png')
jugador1.ancho=100
jugador1.alto=100
jugador1.imagen=pygame.transform.scale(imagenNave, (jugador1.ancho,jugador1.alto))
jugador1.crear(300,400)
jugador1.orientacion=0

#Generamos el Objeto Escenario -----------------------------------------------
fondo= Escenario()
imagenFondo=pygame.image.load('Juego/recursos/fondo.png')
fondo.ancho=700
fondo.alto=500
fondo.imagen=pygame.transform.scale(imagenFondo, (fondo.ancho,fondo.alto))
fondo.crear(0,0)


#---------------------------- fin de espacio  de creacion de los objetos ------------------- 

#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
hecho = False
# Se usa para establecer cuan rápido se actualiza la pantalla (Objeto reloj)
 
reloj = pygame.time.Clock()

# -------- Bucle principal del Programa -----------
while not hecho: #While hecho == False: o defininrlo While hecho != True: 
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key==pygame.K_RIGHT:
                jugador1.movimientos(10,0)
            if evento.key==pygame.K_LEFT:
                jugador1.movimientos(10,1)
            if evento.key==pygame.K_BACKSPACE:
            
    

        
    
    
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
  
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
     
    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    

    pantalla.fill(ROJO)
    pantalla.blit(fondo.imagen, [fondo.puntox, fondo.puntoy])
    pantalla.blit(jugador1.imagen, [jugador1.puntox, jugador1.puntoy])
    
   

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)
     
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()
