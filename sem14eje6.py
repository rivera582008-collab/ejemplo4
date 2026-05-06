import random

def mayores(lista):
    contador = 0
    for i in lista:
        if i > 50 :
            contador += 1
    return contador

numeros = []
for i in range(10):
    numeroaleatorio = random.randint(1,100)
    numeros.append(numeroaleatorio)

print(f"Números generados: {numeros}")

aleatorios = mayores(numeros)
print(f"La cantidad de numeros aleatorios mayores a 50 son: {aleatorios}")
          
    