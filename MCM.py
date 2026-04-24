a = int(input("Ingrese un numero "))
b =  int(input("Ingrese un numero "))

if a > b:
    mcm = a
else:
    mcm = b

while True:
    if mcm % a == 0 and mcm % b == 0:
        break
    mcm += 1
print(f"El MCM de {a} y {b} es: {mcm}")