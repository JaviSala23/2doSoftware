#funciones sin argumentos fijos

def sumar(*args)->int:
    resultado=args[0]
    for numeros in args[1:]:
        resultado=resultado+numeros
    print(resultado)


def restar(*args):
    resultado=args[0]
    for numeros in args[1:]:
        resultado=resultado-numeros
    print(resultado)

def multiplicar(*args):
    resultado=args[0]
    for numeros in args[1:]:
        resultado=resultado*numeros
    print(resultado)

def dividir(*args):
    resultado=args[0]
    for numeros in args[1:]:
        resultado=resultado/numeros
    print(resultado)
    
    

    
    
    
