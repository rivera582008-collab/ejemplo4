def edades(lista):
    contador = 0
    for i in lista:
        if i >= 18:
            contador += 1
    return contador

edadesusuario = []
eda = 0
while eda < 14:
    edadusua = int(input("Ingresen sus edades: "))
    eda += 1
    edadesusuario.append(edadusua)

resultado = edades(edadesusuario)
print(f"La cantidad de personas mayores de edad son: {resultado}")