def suma(a,b):
    resultado= a+ b
    return resultado
    
def resta(a,b):
    resultado=a - b
    return resultado
    
numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese un numero: "))

resultadoSuma=suma(numero1,numero2)
resultadoResta=resta(numero1,numero2)

print(resultadoSuma,resultadoResta)

resutladoDeResultado=suma(resultadoSuma,resultadoResta)
print(resutladoDeResultado)
    
    


