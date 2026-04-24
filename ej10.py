## suma acumulativa con limite
suma = 0
ingresados = []
while True:
    numero = float(input("Ingrese un número: "))
    

    if numero > 0:
        
        ingresados.append(numero)
        suma += numero
    else:
       pass
    
    if suma >= 100:
        print("Saliendo del bucle")
        break
for i in ingresados:
    print("Usted ingreso: ", i)
