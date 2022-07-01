#frutas=["Manzana","Banana","Frutilla","Melon","Sandia"] estas es una forma de  
frutas=["Manzana",
        "Banana",
        "Frutilla",
        "Melon",
        "Sandia"] #esta es otra forma de definir una lista

print(type(frutas)) #imprime el tipo de variable
print(frutas) #imprime los elementos de la lista
print(frutas[0]) #imprime el elemento 1

for elemento in frutas: #recorremos todos los elementos de la lista
    print(elemento) #imprimimos todos los elementos de la lista
    
print(frutas[4]) #imprimimos el ultimo elementos

frutas.append("Peras") #agrega un elemento a la lista

print(frutas) #imprime la lista completa con el elemento nuemos

frutas.remove("Banana")
print(frutas)

frutas.remove(frutas[4])
print(frutas)

