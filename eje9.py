año = int(input("Ingrese un año "))

if año > 9999:
    print(f"El año {año} no es valido")
elif (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")