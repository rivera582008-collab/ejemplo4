## quiero si es lunes dormir hasta las 8
## martes dormir a la 7
## miercoles dormir hasta las 6
## jueves a las 5
## viernes hasta las 4
## sabado si no hay tarea ejercicio
## las funciones son constantes de codigo
## las funciones tienen la posibilidad de introducir parametros inician con def nombre():
## s e dejan cuatro espacios
## if una sola evaliacion
## else por defecto del if
## elif para evaluar multiples acciones
## las funcionesse llaman como seleccionar dia y ()


dia1 = int(input("Seleccione un dia de la semana del 1 al 4 "))


def seleccionardia(dia1):
    if dia1 == 1:
        print("Dormir hasta las 8")
    if dia1 == 2:
        print("Dormir hasta las 9")
    if dia1 == 3:
        print("Dormir hasta las 7")
    if dia1 == 4:
        print("Dormir hasta las 5")
    else:
        print("No Valido")


seleccionardia(dia1)
## validar que sea el formato que espero

nombretramite = ""

nombretramite = input("Ingrese el nombre del tramite ")
nombrecmparacion = (
    input("Ingrese el nombre nuevamente ").lower().strip().replace(" ", "")
)


nombretramite = nombretramite.lower().strip().replace(" ", "")

respuesta = nombretramite.casefold() == nombrecmparacion.casefold()

nombresinnumero = nombretramite.isalnum()

if respuesta and nombresinnumero:
    print("El nombre del tramite es correcto")
else:
    print("Nombre no valido")


# crear una funcion que valide si el nombre esta en mayuscula

nombre = input("Ingrese su nombre")


def nombremayuscula():

    validar = nombre.isupper()
    print(validar)


nombremayuscula()
