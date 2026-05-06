pedidos = [
    {"id": 1, "estado": "pendiente", "prioridad": "baja"},
    {"id": 2, "estado": "entregado", "prioridad": "media"},
    {"id": 3, "estado": "pendiente", "prioridad": "alta"},
    {"id": 4, "estado": "pendiente", "prioridad": "media"},
    {"id": 5, "estado": "pendiente", "prioridad": "baja"},
    {"id": 6, "estado": "entregado", "prioridad": "alta"}
]

repetir = True

while repetir: 
    print("Procesando Pedidos".center(50,"-"))
    
    for p in pedidos:  
        if p["estado"] == "pendiente": 
            
            
            match p["prioridad"]:
                case "alta":
                    print(f"Pedido {p['id']}: ¡Atención inmediata!")
                case "media":
                    print(f"Pedido {p['id']}: Procesar en el día.")
                case "baja":
                    print(f"Pedido {p['id']}: Procesar cuando haya tiempo.")
                case _:
                    print(f"Pedido {p['id']}: Prioridad no definida.")
        else:
            print(f"Pedido {p['id']}: ya está {p['estado']}.")

   
    respuesta = input("¿Deseas volver a procesar la lista? si/no: ").lower()
    if respuesta != "si":
        repetir = False

print("Programa finalizado.")

