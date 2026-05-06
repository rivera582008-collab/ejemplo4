def ordenarMayorMenor(lista):
    numeros = len(lista)
    for i in range(numeros):
        for n in range(0 , numeros - i - 1):
            if lista[n] > lista[n + 1]:
                lista[n], lista[n + 1] = lista[n + 1], lista[n]
    return lista

numeros2 = []
print("Ingrese 6 números: ")
for i in range(6):
    num = int(input(f"Número {i + 1}: "))
    numeros2.append(num)

resultado = ordenarMayorMenor(numeros2)
print("Números de mayor a menor: ",resultado)
        