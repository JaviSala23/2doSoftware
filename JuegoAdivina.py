'''
Juego en donde tenemos que adivinar el numero... u

uso Listas. 
importacion del modulo Random
Condicional compuesto (if elif else)
Loop condicional (while )
interaccion por consola con input()
muestreo por pantalla con print()
'''

import random #trae la libreria random para elementos aleatorios

dado=[1,2,3,4,5,6] #creo una lista de numeros



numeroAleatorio=random.choice(dado) #grabo en la variable un numero aleatorio con random

numero="" #creo la variable numero
contador=0 #creo un contador
while numero!=numeroAleatorio:  #construccion del loop condicional mientras la var numero sea dif de la var numeroAleatorio
    numero=input("Adivine un numero del 1 al 6: ") #cargo un numero
    numero =int(numero) #lo paso a integer
    contador=contador+1 #sumo un intento al contador
    if numero==numeroAleatorio: #compara si los numero son iguales
        print("Usted ha adivinado el numero") #si la comparacion es verdadera imprimo
        print("En: "+ str(contador) + " intentos")

    elif numero>6 or numero<1: #compara si los numero son mayores a 6 o menores a 1 y pido otro numero
        print("El numero esta fuera de rango")

    else: #si no, imprimo que no adivino y pido otro numero
        print("Usted no ha adivinado")

