inventario = [
    {"Nombre": "Manzanas", "Cantidad": 20, "Categoria": "Frutas"},
    {"Nombre": "Naranja", "Cantidad": 40, "Categoria": "Frutas"},
    {"Nombre": "Piña", "Cantidad": 30, "Categoria": "Frutas"},
    {"Nombre": "Mandarina", "Cantidad": 15, "Categoria": "Frutas"},
    {"Nombre": "Pera", "Cantidad": 28, "Categoria": "Frutas"},
    {"Nombre": "Fesa", "Cantidad": 50, "Categoria": "Frutas"},
    {"Nombre": "Sandía", "Cantidad": 20, "Categoria": "Frutas"},
    {"Nombre": "Uva", "Cantidad": 60, "Categoria": "Frutas"},

    {"Nombre": "Leche", "Cantidad": 20, "Categoria": "Lácteos"},
    {"Nombre": "Yogur", "Cantidad": 100, "Categoria": "Lácteos"},
    {"Nombre": "Queso", "Cantidad": 25, "Categoria": "Lácteos"},
    {"Nombre": "Mantequilla", "Cantidad": 29, "Categoria": "Lácteos"},
    {"Nombre": "Crema", "Cantidad": 15, "Categoria": "Lácteos"},
    {"Nombre": "Cuajada", "Cantidad": 36, "Categoria": "Lácteos"},
    {"Nombre": "Requesón", "Cantidad": 20, "Categoria": "Lácteos"},
    {"Nombre": "Flan", "Cantidad": 50, "Categoria": "Lácteos"},

    {"Nombre": "Zanahoria", "Cantidad": 80, "Categoria": "Verduras"},
    {"Nombre": "Lechuga", "Cantidad": 20, "Categoria": "Verduras"},
    {"Nombre": "Cebolla", "Cantidad": 45, "Categoria": "Verduras"},
    {"Nombre": "Brócoli", "Cantidad": 30, "Categoria": "Verduras"},
    {"Nombre": "Espinaca", "Cantidad": 28, "Categoria": "Verduras"},
    {"Nombre": "Pepino", "Cantidad": 90, "Categoria": "Verduras"},
    {"Nombre": "Tomate", "Cantidad": 40, "Categoria": "Verduras"},
    {"Nombre": "Repollo", "Cantidad": 80, "Categoria": "Verduras"}
]
    
    

menu = "BIENVENIDO AL MENÚ DE INVENTARIO".center(60,"-")

while True:
    print(menu)
    print()
    print("1. Listar Productos")
    print("2. Ver Stock Bajo")
    print("3. Ver Por Categoria")
    print("4. Salir")
    print()
    
   
    selecion = input("Ingrese El Número De La Operación A Realizar: ").strip()

    match selecion:
        case "1":
            print("Has Elegido: Listar Productos")
            print()
            print("Listado De Productos".center(40,"_"))
            for producto in inventario:
                nombre = producto["Nombre"]
                cantidad = producto["Cantidad"]
                print(f"Producto: {nombre.ljust(15)} | Stock: {str(cantidad)}")
            print("_" * 40)
           
            input("Presiona Enter Para Continuar: ")

        case "2":
             print("Has Elegido: Ver Stock Bajo".center(50,"!"))
             print()
             limite = 5
             encontrado = False
             for p in inventario:
                  if p["Cantidad"] < limite:
                    print(f"ALERTA: {p['Nombre']} solo tiene {p['Cantidad']} unidades.")
                    encontrado = True
             if not encontrado:
                  print(f"Todo El Stock esta en niveles normales... Mostrando los productos para verificación")
                  print()
                  for i in inventario:
                        nombre = i["Nombre"]
                        cantidad = i["Cantidad"]
                        print(f"Producto: {nombre} Stock: {str(cantidad)}")
 
             input("Presiona Enter Para Continuar: ")
        case "3":
              print("Has Elegido: ver Por Categoria".center(50 , "-"))
              print()
              busqueda = input("Ingrese La Categoria A Buscar ejemplo: Fruta, Verdura, Lácteos, etc: ").lower()
              encon = False
              for i in inventario:
                   if i["Categoria"].lower() == busqueda:
                        nombre = i["Nombre"]
                        cantidad = i["Cantidad"]
                        print(f"Producto: {nombre.ljust(15)} | Stock: {str(cantidad).rjust(3)}")
                        encon = True
              if not encon:
                print(f"No se encontraron productos en la categoria: {busqueda}")

              input("Presiona Enter Para Continuar: ")
        case "4":
               print("Saliendo Del Programa...")
               break
        case _:
              print("⚠️ Opción no válida. Por favor, intenta de nuevo.")
              
         
    
