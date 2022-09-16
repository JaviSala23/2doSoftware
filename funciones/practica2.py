def sumar(numero1, numero2):
    resultado=numero1+numero2
    return resultado

def restar(numero1, numero2):
    resultado=numero1-numero2
    return resultado

def multiplicar(numero1, numero2):
    resultado=numero1*numero2
    return resultado

def dividir(numero1, numero2):
    resultado=numero1/numero2
    return resultado

a=int(input("Ingrese un numero: "))
b=int(input("ingrese otro numero: "))

print("Ingrese 1 para sumar")
print("Ingrese 2 para restar")
print("Ingrese 3 para multiplicar")
print("Ingrese 4 para dividir")

opcion= input("Ingrese una opcion: ")

if opcion=="1":
    resultadoSuma=sumar(a,b)
    print(resultadoSuma)
elif opcion=="2":
    resultadoResta=restar(a,b)
    print(resultadoResta)
elif opcion =="3":
    resultadoMultiplicacion=multiplicar(a,b)
    print(resultadoMultiplicacion)
elif opcion =="4":
    resultadodivicion=dividir(a,b)  
    print(resultadodivicion)  
else:
    print ("Esa opcion no es correcta")
    