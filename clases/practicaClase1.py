
from re import A


class Persona:
    def __init__(self): #funcion COnstructora de objeto que contiene nuestros atributos
        self.nombre=""
        self.apellido=""
        self.peso=0
        self.altura=0
        self.contraseña=""
        self.id=0
        
    
    def saltar(self): #con self llamo a todos los atributos de mi clase
        print("Yo,"+self.nombre+"Estoy Saltando")

    def comer(self):
        print("Estoy comiendo")
    
    def despertar(self):
        print("Estoy despertar")
        
    def estudiar(self):
        print("Estoy estudiar")
        
    def trabajar(self):
        print("Estoy trabajar")


persona1=Persona() #creo un objeto en base a la clase persona que se llama persona1
print(persona1.nombre)
persona1.nombre= "Javier" #cambio el atributo nombre de mi objeto persona1
print(persona1.nombre)
persona1.saltar()
persona1.comer()

    