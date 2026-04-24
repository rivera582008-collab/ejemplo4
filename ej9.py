## juego de adivinar numero

numerodesconocido = 16
inentos = []


while True:
    numero = int(input("¿Adivina el numero que estoy pensando? Pista: esta entre 0 y 20: "))
    
    if numero == numerodesconocido:
        print("FELICIDADES! ADIVINASTE 🎊🎉😁😁")
        break

    inentos.append(numero)
    if numero >= 0 and numero <= 14:
        print("UPSS ESE NO ES SIGUE INTENTANDO 🥱🥱")
        print("Un poco mas alto")
    
    elif numero == 15:
        print("UPSS ESE NO ES SIGUE INTENTANDO 🥱🥱")
        print("Un poquitito más casi lo tienes!! 😨😨🙀🙀")

    
    elif numero >= 17 and numero <= 20:
        print("UPSS ESE NO ES SIGUE INTENTANDO 🥱🥱")
        print("Un poquito menos 😳")
    

for i in inentos:
    print(f"Tus intentos fueron: {i}")
