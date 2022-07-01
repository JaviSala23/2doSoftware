import random #trae la libreria random para elementos aleatorios

dado=[1,2,3,4,5,6]

numero=input("Adivine un numero del 1 al 6: ")
numero =int(numero)
numeroAleatorio=random.choice(dado)

if numero==numeroAleatorio:
    print("Usted ha adivinado el numero")

elif numero>6 or numero<1:
    print("El numero esta fuera de rango")

else:
    print("Usted no ha adivinado")

