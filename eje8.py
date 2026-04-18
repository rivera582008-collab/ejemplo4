lado1 = float(input("Ingrese la medida de un lado del triangulo: "))
lado2 = float(input("Ingrese la medida del segundo lado del triangulo: "))
lado3 = float(input("Ingrese la medida del tercer lado del triangulo: "))

if lado1 == lado2 == lado3:
    print("El triángulo es Equilátero (todos sus lados son iguales)")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triángulo Isósceles (Dos de sus lados son iguales)")
else:
    print("Es un triangulo Escaleno (Todos sus lados son diferentes)")