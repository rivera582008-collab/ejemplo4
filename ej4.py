## suma de numeros impares 
n = 0
impares = []

while True:
    numero = float(input("Ingrese un número: "))
    numeroarreglado = int(numero)

    if numeroarreglado == 0:
        print("Bucle finalizado")
        break

    if numeroarreglado % 2 != 0:
        impar = n + numeroarreglado
        n = impar
        impares.append(numeroarreglado)


for i in impares:
   
   print(f"Los impares ingresados son: {i}")
       
print(f"La suma de todos los impares es: {n}")
