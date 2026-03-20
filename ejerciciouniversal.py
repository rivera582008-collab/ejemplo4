nombre = input("Ingrese su nombre completo")
nombreMayusculas = nombre.upper()
print(nombreMayusculas)

nombreMinusculas = nombre.lower()
print(nombreMinusculas)

nombreCaracteres = len(nombre)
print("cantidad de caracteres", nombreCaracteres)

frase = input("Ingrese su frase favorita")
print(frase)

fraseMayusculas = frase.upper()
print(fraseMayusculas)

fraseMinuscula = frase.lower()
print(fraseMinuscula)

frase = input("Ingrese su frase favorita")
quitarEspacios = frase.replace(" ", "")
print(quitarEspacios)

letrasSinEspacio = len(quitarEspacios)
print("la cantidad de caracteres es", letrasSinEspacio)

correo = input("Ingrese su correo electronico")

if "@" in correo:
    print("El correo parece valido")
else:
    print("El correo no es valido")

frase = input("Inrese una frase").strip()

primeraLetra = frase[0]
ultimaLetra = frase[-1]
print("la primera letra es", primeraLetra)
print("la ultima letra es", ultimaLetra)

nombre = input("Ingrese su nombre completo")
nombreSeparado = nombre.split()

for p in nombreSeparado:
    print(p)

frase = input("Ingrese una frase")
fraseMinuscula = frase.lower()

fraseSustituida = fraseMinuscula.replace("python", "programacion")
print(fraseSustituida)

frase = input("Ingree una frase")
minuscula = frase.lower()
conteo = minuscula.count("a")
print("En su frase la letra a esta presente", conteo, "veces")

frase = input("Ingree una frase").strip()
minuscula = frase.lower()
metodo = minuscula.startswith("hola")
if metodo:
    print("la frase comienza con hola")
else:
    print("La frase no comienza con hola")

frase = input("Ingrese una frase").strip()
metodo = frase.endswith(".")
if metodo:
    print("La frase termina con .")
else:
    print("La frase no termina con .")
