edad = int(input("Ingrese su edad"))

if edad >= 0 and edad < 18:
    print("Usted es menor de edad")
elif edad >= 18 and edad < 35:
    print("Usted es mayor de edad")
elif edad >= 35 and edad <= 100:
    print("Usted es un adulto mayor")
else:
    print(f"{edad} no es correcto ingrese una edad valida")
