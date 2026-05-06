def listaDeNumeros(lista):
     
    pares = 0
    impares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares


lista = []
intentos = 0
    
while intentos < 20:
    lista2 = int(input("Ingrese un numero: "))
    intentos += 1
    lista.append(lista2)


pares , impares = listaDeNumeros(lista)

print(f"Los pares de la lista son: {pares}")
print(f"Los impares de la lista son: {impares}")


