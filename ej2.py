## Contador de positivos y negativos
ingresados = []

while True:
    numero = float(input("Ingrese un número: "))
    numeroarreglado = int(numero)

    if numeroarreglado == 0:
        print("Bucle finalizado")
        break

    ingresados.append(numeroarreglado)

positivos = 0
negativos = 0

for i in ingresados:
    if i > 0:
        positivos += 1
    elif i < 0:
        negativos += 1

print(f"Total de numero positivos ingresados: {positivos}")
print(f"Total de numeros negativos ingresados: {negativos}")
