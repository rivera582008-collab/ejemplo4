def nombresCaracteres(lista):
    print("Mostrando nombres con más de 5 carácteres".center(50, "*"))
    for i in lista:

        if len(i) > 5:
            print(i)
 


listanombres = []
contador = 0

while contador < 10:
    nombres = input("Ingrese un nombre: ").strip().replace(" ", "")
    contador += 1
    listanombres.append(nombres)

nombresCaracteres(listanombres)


