

class Mamifero:
    def __init__(self):
        self.peso=0
        self.energia=0
        self.edad=0
        self.altura=0
        self.salud=0
    
    def alimentarse(self):
        print("se ha alimentado, sube 10 puntos de energia")
        self.energia= self.energia+10
    
    def reproducirse(self):
        print("sobrevivira la especie!!!")
        
    def crecer():
        print("ya es adulto!")      
        

class Leon(Mamifero):
    def __init__(self):
        self.color="marron"
        self.genero=""
        self.poscionManada="alfa"
        self.dentadura="afilado"
    
    def cazar():
        print("obtuvo una zebra")
        