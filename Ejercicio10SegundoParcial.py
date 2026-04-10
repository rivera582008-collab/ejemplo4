texto = "Python2026"

if texto.isalnum():
    minusculas = texto.lower()
    palabra = minusculas.replace("2026", " 2026")
    print(palabra)
    print(palabra.replace("2026", ""))
