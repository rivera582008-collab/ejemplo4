def numeroMayor(lista):
    mayor = lista[0]
    for n in lista:
        if n > mayor:
            mayor = n
    return mayor


num = []
contador = 0

while contador < 8:
    numeros = float(input("Ingrese un número: "))
    contador += 1
    num.append(numeros)

mayor = numeroMayor(num)
print(f"El número mayor de la lista es: {mayor}")
