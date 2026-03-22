frase = input("Ingrese una frase").strip()
metodo = frase.endswith(".")
if metodo:
    print("La frase termina con .")
else:
    print("La frase no termina con .")
