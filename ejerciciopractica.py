nombre = input("ingrese un nombre").strip().lower()
apellido = input("Ingrese un apellido").strip().lower()
cortado = apellido.split()
final = cortado[0]
PrimeraLetra = nombre[0]

usuario = PrimeraLetra + final
print("Su nuevo usuario sera", usuario)
caracteres = len(usuario)
print("Su nuevo usuario costa de", caracteres, "Caracteres")


precioMalo = input("Ingrese el precio del producto").strip()
precioCorrecto = precioMalo.replace(",", ".")
precioPrueba = precioCorrecto.replace(".", "")
precioBueno = precioPrueba.isdigit()


if precioBueno == True:
    print("El precio es correcto", precioCorrecto)
else:
    print("Ingrese correctamente el precio", precioMalo, "No es correcto")


frase = input("Ingrese una frase").lower()
PalabraE = frase.count("e")
print(f"La vocal E aparece {PalabraE} veces")

if "secreto" in frase:
    print("¡Cuidado! Esta frase contiene información confidencial")
else:
    print("Frase segura \°,,°/")


saldo = 2000


while saldo > 0:

    print(f"Bienvenido tu saldo actual es de {saldo}")
    retirarDinero = int(input("Cuanto dinero desea retirar"))

    if retirarDinero < 0:
        print("Eror ingrese un numero valido")
        break
    elif retirarDinero <= saldo:
        saldoDespues = saldo - retirarDinero
        print(f"Retiro exitoso. Tu nuevo saldo es ${saldoDespues}")
        saldoActual = saldoDespues
        saldo = saldoActual

    else:
        print(
            "¡Error! Usted no cuenta co suficiente dinero para realizar la transacción"
        )
        break
