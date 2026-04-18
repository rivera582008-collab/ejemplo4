notas = int(input("Ingrese la nota del estudiante"))

if notas == 9 or notas == 10:
    print(f"El estudiante obtuvo un {notas} EXCELENTE")
elif notas == 7 or notas == 8:
    print(f"El estudiante obtuvo un {notas} BUENO ")
elif notas == 6:
    print(f"El estudiante saco un {notas} APROBADO pero debe mejorar")
elif notas >= 0 and notas <= 5:
    print(f"El estudiante saco {notas} lamentablemente el estudiante esta REPROBADO")
else:
    print("Ingrese una nota valida")
