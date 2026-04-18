numero1 = int(input("Ingrese un número "))

numero2 = int(input("Ingrese un segundo número "))

operador = input("Ingrese un operador (- , + , * , /) ").strip()

if operador == "-":
    print(f"El resultado de la resta es: {numero1 - numero2}")
elif operador == "+":
    print(f"El resultado de la suma es {numero1 + numero2}")
elif operador == "*":
    print(f"El resultado de la multiplicación es {numero1 * numero2}")
elif operador == "/":
    if numero2 == 0:
        print("La división por cero no existe")
    else:
        print(f"El resultado de la división es {numero1 / numero2}")
else:
    print("Ingrese un número y operador valido")
