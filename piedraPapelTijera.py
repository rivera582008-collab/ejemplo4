import random
import os

# Esta función srve para limpiar la pantalla y se llama con import os y luego con os.system('cls' if os.name == 'nt' else 'clear') dependiendo del sistema operativo que se esté utilizando, para limpiar la pantalla antes de cada turno y al inicio del juego.
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

nombre = input(" 🖐 🖐  Bienvenido/a, ingrese su nombre para empezar a jugar: ")

def juego():
    
    limpiar()
    print(f" 😄 😄 Bienvenido/a {nombre} al juego guerra de animales 🦁🐱‍🐉🐍🐀🐦🐉🧸🦈")

    print("-" * 50)
    print("📜 REGLAS DE VICTORIA: 📜".center(50))
    print("-" * 50)
    print("1. Dinosaurio 🦖 vence a: León y Serpiente")
    print("2. León       🦁 vence a: Serpiente y Ratón")
    print("3. Serpiente  🐍 vence a: Ratón y Águila")
    print("4. Ratón      🐭 vence a: Águila y Dinosaurio")
    print("5. Águila     🦅 vence a: Dinosaurio y Dragón")
    print("6. Dragón     🐲 vence a: Oso y León")
    print("7. Oso        🐻 vence a: Megalodón y Serpiente")
    print("8. Megalodón  🦈 vence a: Dragón y Dinosaurio")
    print("-" * 50)
    input("Presiona ENTER para empezar a jugar...")

    empates = 0
    victorias = 0
    derrotas = 0
    contador = 0
    
    while contador < 14:
        limpiar() 
        print("-" * 100)
        print("1--Dinosaurio")
        print("2--Leon")
        print("3--Serpiente")
        print("4--Ratón")
        print("5--Águila")
        print("6--Dragón")
        print("7--Oso")
        print("8--Megalodón")
        
        ataquejugador = int(input("seleccione una opción ingresando un número entre 1 y 8: "))

        ataquecomputadora = random.randint(1,8)
        
        ataque = ""
        if ataquecomputadora == 1:
            ataque = "Dinosaurio"
        elif ataquecomputadora == 2:
            ataque = "Leon"
        elif ataquecomputadora == 3:
            ataque = "Serpiente"
        elif ataquecomputadora == 4:
            ataque = "Ratón"
        elif ataquecomputadora == 5:
            ataque = "Águila"
        elif ataquecomputadora == 6:
            ataque = "Dragón"
        elif ataquecomputadora == 7:
            ataque = "Oso"
        else:
            ataque = "Megalodón"

        ataque2 = ""
        if ataquejugador == 1:
            ataque2 = "Dinosaurio"
        elif ataquejugador == 2:
            ataque2 = "Leon"
        elif ataquejugador == 3:
            ataque2 = "Serpiente"
        elif ataquejugador == 4:
            ataque2 = "Ratón"
        elif ataquejugador == 5:
            ataque2 = "Águila"
        elif ataquejugador == 6:
            ataque2 = "Dragón"
        elif ataquejugador == 7:
            ataque2 = "Oso"
        elif ataquejugador == 8:
            ataque2 = "Megalodón"
        else:
            print("ingrese un número válido entre 1 y 8.")
            pass
            
        contador += 1
        
        if ataque == ataque2:
            print(f"Computadora ataco con {ataque} y tu {nombre} con {ataque2} EMPATE 🤝🤝")
            empates += 1
        elif ataquejugador == 1 and (ataquecomputadora == 2 or ataquecomputadora == 3):
            print(f"Computadora ataco con {ataque} y tu {nombre} con {ataque2} FELICIDADES GANASTE!! 🎉🎉")
            victorias += 1
        elif ataquejugador == 2 and (ataquecomputadora == 3 or ataquecomputadora == 4):
            print(f"Computadora ataco con {ataque} y tu {nombre} con {ataque2} FELICIDADES GANASTE!! 🎉🎉")
            victorias += 1
        elif ataquejugador == 3 and (ataquecomputadora == 4 or ataquecomputadora == 5):
            print(f"Computadora ataco con {ataque} y tu {nombre} con {ataque2} FELICIDADES GANASTE!! 🎉🎉")
            victorias += 1
        elif ataquejugador == 4 and (ataquecomputadora == 5 or ataquecomputadora == 1):
            print(f"Computadora ataco con {ataque} y tu {nombre} con {ataque2} FELICIDADES GANASTE!! 🎉🎉")
            victorias += 1
        elif ataquejugador == 5 and (ataquecomputadora == 1 or ataquecomputadora == 6):
            print(f"Computadora ataco con {ataque} y tu {nombre} con {ataque2} FELICIDADES GANASTE!! 🎉🎉")
            victorias += 1
        elif ataquejugador == 6 and (ataquecomputadora == 7 or ataquecomputadora == 2):
            print(f"Computadora ataco con {ataque} y tu {nombre} con {ataque2} FELICIDADES GANASTE!! 🎉🎉")
            victorias += 1
        elif ataquejugador == 7 and (ataquecomputadora == 8 or ataquecomputadora == 3):
            print(f"Computadora ataco con {ataque} y tu {nombre} con {ataque2} FELICIDADES GANASTE!! 🎉🎉")
            victorias += 1
        elif ataquejugador == 8 and (ataquecomputadora == 6 or ataquecomputadora == 1):
            print(f"Computadora ataco con {ataque} y tu {nombre} con {ataque2} FELICIDADES GANASTE!! 🎉🎉")
            victorias += 1
        else:
            print(f"La computadora ataco con {ataque} y tu {nombre} con {ataque2} UPSS PERDISTE 😞😞")
            derrotas += 1
            
        print("-" * 100)
        input("Presiona ENTER para continuar...") 

    print(f"El juego ha terminado, {nombre}!! resumen de tus resultados:".center(100))
    print("-" * 100)
    print(f"Victorias: {victorias} | Derrotas: {derrotas} | Empates: {empates}")
    print("_" * 100)

    jugardenuevo = input("¿Quieres volver a jugar? Escribe 'si' o 'no': ").lower().strip()
    if jugardenuevo == "si":
        juego()
    else:
        print("Gracias por jugar, hasta la próxima!! 👋👋")

juego()