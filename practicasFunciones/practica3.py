from funciones.funcionesArgumentos import *

listaDeArgumentos=[]
for l in range(3):
    a=int(input("Ingresar un numero: "))
    listaDeArgumentos.append(a)
   
sumar(listaDeArgumentos[0],listaDeArgumentos[1],listaDeArgumentos[2])

listaDeArgumentos=[]
for l in range(5):
    a=int(input("Ingresar un numero: "))
    listaDeArgumentos.append(a)
    
restar(listaDeArgumentos[0],listaDeArgumentos[1],listaDeArgumentos[2],listaDeArgumentos[3],listaDeArgumentos[4])

multiplicar(4,56)

a=int(input("Ingresar un numero: "))
n=int(input("Ingresar un numero: "))
dividir(a,n)


