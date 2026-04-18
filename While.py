intentos = 0
Correcto = 8


while intentos < 10:
    numero = int(input("Adivina el numero entre 1 y 10 "))
    if numero < 0 or numero > 10:
        print("Numero no valido")
        intentos += 1

    elif numero == Correcto:
        print("Adivinaste")
        break
    elif intentos == 10:
        break

    else:
        intentos += 1
        print("Sigue intentando")
        
        

