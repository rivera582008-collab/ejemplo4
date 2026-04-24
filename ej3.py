## Tabla de multiplicar filtrada

while True:
    numero = float(input("Ingrese un número: "))
    numeroarreglado = int(numero)

    if numeroarreglado < 0:
        print("Bucle finalizado")
        break

    print(f"Tabla del: {numeroarreglado}")
    print("-" * 40)
    print(f"Mostrando solo los resultados mayores a 20 de la tabla del: {numeroarreglado}")

    encontrado = False

    for i in range(1, 11):
        resultado = numeroarreglado * i
        if resultado > 20:
            print(f"{numeroarreglado} x {i} = {resultado}")
            encontrado = True
    
    if not encontrado:
        print(f"La tabla del: {numeroarreglado} no tiene resultados mayores a 20")
