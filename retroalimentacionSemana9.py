Serie = "fullmetal alchemits"

### cada variable tiene un espacio de memoria asignado

## cuando una vable cambia => se pierde la inmutabilidad
## POO
## polimorfismo -> es el cambio de acciones sin que se rompa el codigo
## abstracciones ->
##      Tasa de cafe
#       cafe coscafe
##       azucar
##      agua
##      otros ingredientes
##  un objeto es el que toma un modelo y este modelo le da funciones y utiliza sus propiedades

## Leon ->
## tiene ojos  (propiedades)
## tiene boca
## Esta guapo
#############
#  corre        ( Funciones )
# salta

## Clases
## Estructura de datos.


## es arreglo es una variable que tiene adentro otra variable
## Listas.
## Arrays.-> se inia a contar desde el 0
## tuplas.
## indices.


# -------------------------------------------------------
def saludo(nombres):
    print(nombres)


# saludo(Serie) las funciones simpre van  a tener ()
# -------------------------------------------------------
## las funciones tienen un espacio
## Scope es dond reciden las variables

## Colocar el nombre de la serie como titulo
fmaTemu = Serie.title()
# saludo(Serie)
# saludo(fmaTemu)
fnaMayusculas = Serie.upper()
saludo(fnaMayusculas)
## deprogracion Lineal
FullmetalCapitalizer = fnaMayusculas.swapcase().title()
## cuando encadenamos funciones se indica que la salidad de la funcion actual
# 3 es la entrada de la siguiente funcion.

saludo(FullmetalCapitalizer)

## compara cadenas de texo
comparar1 = "Ever"
comparar2 = "Ever"

# casefold para comparar y pasar a  minusculas
variableTemporal = comparar2.casefold()
comparar = comparar1.casefold() == comparar2.casefold()
# print(comparar)
## casefold nos dara true unicamente si los elementos son identicos sino nos indcara un false

## para verificar si es nu nuemero o un caracter vamos a utilizar isalfa()
clasicas2005 = "Gasolina"
comprarisAlpha = clasicas2005.isalpha()
# print(comprarisAlpha, 2005)
# isalpha nos va a dar true si el string que se le esta enviando es unicamente letras
# solo numeros isalnum
letracancion = "lo que paso paso entre tu y yo"
decada = "10"

ejemplo = letracancion.isalnum()
print(ejemplo)

ejemplo = decada.isalnum()
print(ejemplo)
# isalnum es para compara solo numeros dara true cuandoh aya solo numeros
comprobardecadas = decada.isdigit()
print(comprobardecadas)


nombre = input("Escriba su nombre completo")
nombreMayusculas = nombre.upper()
print(nombreMayusculas)
nombreMinusculas = nombre.lower()
print(nombreMinusculas)
nombreprimeraletramayuscula = nombre.title()
print(nombreprimeraletramayuscula)
