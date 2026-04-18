numero = int(input("Ingrese un número"))

if numero < 0:
    print(f"El número {numero} es negativo")
elif numero > 0:
    print(f"El numero {numero} es positivo")
elif numero == 0:
    print("El numero ingresado es igual a cero")
else:
    print("Ingrese un numero valido")

