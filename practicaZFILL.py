texto = input("Ingrese una palabra ").ljust(10, "-")


print(texto)

texto1 = input("Ingrese una palabra ").rjust(10, "-")


print(texto1)

texto2 = input("Ingrese una palabra ").center(20, "-")


print(texto2)

texto3 = input("Ingrese un numero ")
text = texto3.strip().zfill(6)

print(text)    


f1 = "Manzana".ljust(20)    
f2 = "Pera".ljust(20)
f3 = "Mango".ljust(20)
f4 = "Melon".ljust(20)
f5 = "Sandia".ljust(20)
f6 = "Fresas".ljust(20)

print(f2 , "1000")
print(f3 , "1000")
print(f4 , "1000")
print(f5 , "1000")
print(f6 , "1000")


productos = [("Manzana" , 2.5) , ("pera" , 3.4) , ("Mango" , 2.3) , ("Papa" , 5.5) , ("Pepino" , 7.5) , ("Jocote" , 4.2) , ("Fresa" , 6.5) , ("Melon" , 2.6) ]

print(f"{'PRODUCTO' :<12} | {'PRECIO' :>8}")
print("-" * 25)

for nombre, precio in productos:
    print(f"{nombre:<12} | {precio:>8.2f}" )



