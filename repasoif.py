def pedirNumero():
    numero = input("Ingrese un numero: ")
    return numero

def validarNumero(numero):
    validarn = numero.isdigit()
    return validarn
def paroimpar(numero):
     if numero % 2 == 0:
        print("El numero es par")
     elif numero % 2 != 0:
        print("El numero es impar")

def buclewhile(intentos):
    control = True
    contador = 0
    while control:
        seleccion = pedirNumero()
        validado = validarNumero(seleccion)
        paroimpar(validado)
        contador += 1
        
        if contador == intentos:
            control = False
buclewhile(3)

## variables globales van al principio del codigo
# parse es convertir na variable de un tipo a otro
## pedir numero 2- validar que sea un numero
## indicar si es par o impar
## while es un bucle los bucles necesitan algo que los rompa
## buleanos verdadero o falso
## refactorizar el codigo
## creacion de funciones

semana = ["lunes", "martes", "miercoles", "jueves", "Viernes"]

sele = int(input("seleccione un dia de la semana del 1 al 7 "))

for i in range(len(semana)):
    if sele == i + 1:
        print(semana[i])
## un array es una variable que tiene un indice y un contenido
## es una variable global que se puede usar en cualquier parte del programa
def validarNumero(numero):
    validarn = numero.isdigit()
    return validarn
def validarrango(numero):
    va = int(numero) >= 0 and int(numero) <= 6
    return va

def mo(numero):
    match numero:
        case 1:
            print(semana[0])
        case 2:
            print(semana[1])
        case 3:
            print(semana[2]) 
        case 4:
            print(semana[3])
        case 5:
            print(semana[4])  

def armarfucion():
    dia = pedirNumero()
    validardia = validarNumero(dia) 
    validarran = validarrango(dia)
    if validardia and validarran:
        mo(int(dia))
    else:
        print("El numero ingresado no es valido")
armarfucion()


def solicitarpalabra():
    palabra = input("Ingrese una palabra ").lower()
    return palabra

def listaacompletar(palabraacomparar):
    listaaCompletar = [None] * len(palabraacomparar)
    return listaaCompletar
def solicitarLetra():
    letra = input("Ingrese una letra: ").lower()
    return letra

def compararListas(palabraacomparar, listaaCompletar):
    letra = solicitarLetra()
    for i, palabratemporal in enumerate(palabraacomparar):
        if letra in palabratemporal:
            listaaCompletar[i] = letra
    return listaaCompletar

def definirintentos(PalabraAEncontrar):
    intentos = int(input("Ingrese la cantidad de intentos: "))
    return intentos + len(PalabraAEncontrar)

def Aplicarbucle():
    contador = 0
    palabraadivinar = solicitarpalabra()
    listacompletar = listaacompletar(palabraadivinar)
    intentos = definirintentos(palabraadivinar)
    while contador < intentos:
        lista = compararListas(palabraadivinar,listacompletar)
        print("".join([sustituir if sustituir is not None else "_" for sustituir in lista]))
        contador += 1
        print(f"Te quedan {intentos - contador} intentos")

Aplicarbucle()





#palabra = solicitarpalabra()
#print(palabra)
## una lista va a tener 0 o muchos elementos