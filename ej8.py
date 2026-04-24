## patron de asteriscos

while True:
    numero = float(input("Ingrese la altura que desea que tenga el triánguo: "))
    numeroarreglado = int(numero)

    if numeroarreglado == 0:
        print("Bucle finalizado")
        break


    for i in range(1, numeroarreglado + 1):

        if i % 2 != 0:
            fila = "*" * i
            print(fila.center(numeroarreglado))

                
    