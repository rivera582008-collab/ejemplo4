def sumapares(lista):
    pares = []
    for i in lista: 
        if i % 2 == 0:
            pares.append(i)
            
    return pares



parsumado = []
ingresados = 0
while ingresados < 20:
    pedirusuario = float(input("Ingrese un número: "))
    ingresados += 1
    parsumado.append(pedirusuario)


resultadoparcial = sumapares(parsumado)
resultadofinal = sum(resultadoparcial)
print(resultadofinal)