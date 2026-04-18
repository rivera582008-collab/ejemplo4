def precio():
    if compra > 100:
        descuento20 = compra * 0.2
        resultado1 = compra - descuento20
        print(f"Obtuvo un 20% de descuento, su total a pagar es de: {resultado1}")
    elif compra >= 50 and compra <= 100:
        descuento10 = compra * 0.1
        resultado2 = compra - descuento10
        print(f"Obtuvo un 10% de descuento, su total a pagar es de: {resultado2}")
    else:
        print(f"Su total a pagar es de: {compra}")


compra = float(input("Ingrese el total de la compra "))
        
precio()





