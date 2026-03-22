frase = input("Ingree una frase").strip()
minuscula = frase.lower()
metodo = minuscula.startswith("hola")
if metodo:
    print("la frase comienza con hola")
else:
    print("La frase no comienza con hola")
