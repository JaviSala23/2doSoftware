#carpeta Lib dentro de la carpeta juego
# la palabra reservada pass sirve para decirle a python que no tenemos codigo escrito aun para nuestra funcion, sin esta palabra 
# el programa tira error.


#definimos la clase abstracta y super clase ELEMENTOS
class Elementos: 
    #atributos creado con su constructor (def __init__)
    def __init__(self):
        self.imagen=""
        self.puntox=0
        self.puntoy=0
        self.ancho=0
        self.largo=0
        self.orientacion=""
     
    #funciones de la clase elementos    
    def destruir(self):
        pass
    
    def crear(self):
        pass   
# fin de clase Elementos


#definimos clase Nave (hereda de Elementos)
class Nave(Elementos):
    
    def disparar(self):
        pass
   
# fin d clase Nave

#definimos clase Jugador (hereda de Elementos y Nave)    
class Jugador(Nave):
    
    def __init__(self):
        self.botonDerecha="KEY_RIGHT"
        self.botonIzquierda="KEY_LEFT"
        self.botonDisparo="KEY_A"
    
    def movimientos(self,x):
        pass
    
#fin d clase Jugador

#definimos clase Enemigo (hereda de Elementos y Nave)
  
class Enemigo(Nave):
    
    def movimientos(self,x,y):
        pass
    
    def inteligenciaArtificial(self):
        pass
     
#fin d clase Enemigo    
     
#definimos clase Misil (hereda de Elementos )     
class Misil(Elementos):
    
    def movimientos(self,y) :
        pass  

#fin d clase Misil     

#definimos clase Escenario (hereda de Elementos )  
class Escenario(Elementos):
    
    def movimientos(self,y) :
        pass  
    
    def cambioFondo(self,y) :
        pass  

#fin de clase Escenario