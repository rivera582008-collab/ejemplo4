## Números primos en rango

while True:
    numero = float(input("Ingrese un número: "))
    numeroarreglado = int(numero)

    if numeroarreglado <= 0:
        print("Bucle finalizado")
        break

    if numeroarreglado <= 1:
        print("No es primo")
    else:
        esprimo = True

        for i in range(2, numeroarreglado):

            if numeroarreglado % i == 0:
                esprimo = False
                break
        if esprimo:
            print(f"{numeroarreglado} es un número primo")

        else:
            print(f"{numeroarreglado} no es un número primo")
            print("*" * 40)

   