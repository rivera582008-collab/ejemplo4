# si tenemos una variable y necesitamos comprobar si cumple un criterio hacemos

clima = "caliente"

entrada = input("¿como esta el clima?").strip().lower()
# print("El clima es: ", entrada)
if entrada == "frio":
    print("comprar algodn de azucar".title())
elif entrada == "caliente":
    print("Comprar Un Licuado")
else:
    print("No valido")

# if es para tomar una decisión
# para igualar un valor vamos a tomar el ==

edad = 7
if edad >= 21:
    print("Deberias trabajar Para Darle Regalos A Tus Nietos")
else:
    print("Cuida tus rodillas")

# if verifica un camino si este camino no esta  else deduce una acción por defecto

numero = 50

if numero > 24 and numero < 30:
    print("en numero es mayor que 24 y menor que 30")
elif numero >= 30 and numero < 40:
    print("el numero es mayor a 30")
elif numero > 35:
    print("Cliente vip")
else:
    print("no puedes entrar")

# en un rango de numeros entre 10 y 100 vamos a verificar un segmento entre
# 18 mayor de edad
# 25 adulto joven
# 40 adulto
# 60 adulto mayor

edad2 = int(input("inggrese su edad: "))

edadnumerica = int(edad2)

if edadnumerica >= 10 and edadnumerica < 18:
    print("Usted es un niño/a")
elif edadnumerica >= 18 and edadnumerica < 25:
    print("Mayor de edad")
elif edadnumerica >= 25 and edadnumerica < 40:
    print("Eres un adulto joven")
elif edadnumerica >= 40 and edadnumerica < 80:
    print("eres un adulto")
elif edadnumerica >= 80 and edadnumerica < 100:
    print("Señor de tercera edad")
elif edadnumerica >= 100:
    print("marciano")
else:
    print("No encontrado")


def cambiarFormato(edad3):
    if edad3.isdigit():
        return edad3
    else:
        print("La edad debe ser un numero")
