## Validación de contraseña 

contraseña = "R2085AML"
intentos = []

while True:
    contraseña1 = input("Ingrese su contraseña: ")
    
    if contraseña1 == contraseña:
        print("Su contraseña es correcta")
        break
    else:
        print("contraseña incorrecta")
    intentos.append(contraseña1)
    



fracasos = 0
for f in intentos:
    fracasos += 1
print(f"Usted tuvo {fracasos} intentos fallidos")