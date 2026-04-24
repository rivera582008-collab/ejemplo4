## promedio de notas
sumanotas = 0
notasingresadas = []
while True:
    nota = float(input("Ingrese una nota: "))

    if nota == -1:
        print("Bucle finalizado")
        break
    elif nota < 0 or nota > 10:
        pass
    else:
        sumanotas += nota
        
        notasingresadas.append(nota)

for notas in notasingresadas:
    promedio = len(notasingresadas)
    promedioreal = sumanotas / promedio
print(f"Su promedio final es de: {promedioreal}")
