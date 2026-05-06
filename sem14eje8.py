def buscador(producto,productosolicitado):
    for i in producto:
        if i == productosolicitado:
            return "Producto encontrado"
    return "Producto no encontrado"

productos = []
for i in range(5):
    productosusuario = input("Ingrese el nombre del producto: ").strip().lower()
    i += 1
    productos.append(productosusuario)

busqueda = input("Que pruducto desea buscar: ").strip().lower()

resultado = buscador(productos,busqueda)
print(resultado)
