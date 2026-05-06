def notas(n): 
    promedio = sum(n) / len(n)
    if promedio >= 6:
        resultado = "el grupo Aprobo"
    else:
        resultado = "el grupo reprobo"
    return promedio, resultado
        
    


notasCantidad = []
contador = 0

while contador < 10:
    notas2 = float(input("Ingrese las notas de los estudiantes: "))
    contador += 1
    notasCantidad.append(notas2)

promedio , resultado = notas(notasCantidad)
print(f"El promedio es {promedio} por lo tanto {resultado}")

