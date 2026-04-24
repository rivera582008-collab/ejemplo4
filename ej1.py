## Números pares en rango

while True:
    numero = float(input("Ingrese un número, el número debe ser un entero: "))
    numeroarreglado = int(numero)

    if numeroarreglado <= 0:
        print("Bucle finalizado")
        break

    for i in range(1, numeroarreglado + 1):

        if i % 2 == 0:
            print(f"Par: {i}")
    print("*" * 40)
    