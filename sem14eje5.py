def numerosPositivos(lista):
    positivos = []
   
    for po in lista:
        if po > 0:
            positivos.append(po)
    return positivos 

arreglo = [1,2,3,-2,-3,-4,4,5,6,7,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8]
positivos = numerosPositivos(arreglo)
print(f"positivos {positivos}")
