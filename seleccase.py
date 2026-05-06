
## ingresar una cantidad par de numeros
## emparejarlas con un texto
## numero de intentos definidos para el usuario
## prepararel bucle y el selec case
## las tarjetas se deben mezclar

import random # esto es para numero aeatorios

numero = random.randint(1,10)



def definirtarjetas(numero):
    if numero % 2 == 0 and numero > 4:
        return numero
    else:
        return numero + 1
    
def asignarvaloresalastarjetas(numerovalidado):
    i = 0
    llenartarjetas = []
    temporal = ""
    while i <= numerovalidado:
        temporal = input("Ingrese el valor de la tarjeta: ")
        llenartarjetas.append(temporal)
        i += 1
    return llenartarjetas

def realizarlistadeintentos(tarjetasconvalor):
    intentos = 0
    propuestadelusuario = []
    while intentos <= len(tarjetasconvalor):
        propuestadelusuario.append(input("ingrese el texto para la propuesta: "))
        intentos += 1



def validartarjetas(propuestadelusuario, llenartarjetas):
    i = 0
    for i in range(len(llenartarjetas)):
     
        match i:
            case 1:
                if llenartarjetas[1] == propuestadelusuario[1]:
                    print("Ganaste")
            case 2:
                 if llenartarjetas[2] == propuestadelusuario[2]:
                    print("Ganaste")
            case 3:
                 if llenartarjetas[3] == propuestadelusuario[3]:
                    print("Ganaste")

            case 4:
                 if llenartarjetas[4] == propuestadelusuario[4]:
                    print("Ganaste")

            case 5:
                 if llenartarjetas[5] == propuestadelusuario[5]:
                    print("Ganaste")
            case 6:
                 if llenartarjetas[6] == propuestadelusuario[6]:
                    print("Ganaste")
            case 7:
                 if llenartarjetas[7] == propuestadelusuario[7]:
                    print("Ganaste")

            case 8:
                 if llenartarjetas[8] == propuestadelusuario[8]:
                    print("Ganaste")
            
            case 9:
                 if llenartarjetas[9] == propuestadelusuario[9]:
                   print("Ganaste")
            case 10:
                 if llenartarjetas[10] == propuestadelusuario[10]:
                    print("Ganaste")
            case _:
                print("Perdiste")
        i+= 1


def iniciarjuego():
    estadojuego = True
    while estadojuego:

        numerovalido = definirtarjetas(numero)
        pllenartajetas = asignarvaloresalastarjetas(numerovalido)
        propuestadeusuaro = realizarlistadeintentos(pllenartajetas)
        validartarjetas(propuestadeusuaro,pllenartajetas)
        estdo = input("Desea jugar de nuevo (s/n) ")
        if estdo == "s":
            continue
        else:
            break
iniciarjuego()
import tkinter as tk
def saludar():
    print("¡Hola hiciste un boton!")

ventana = tk.Tk()
ventana.title("Ejemplo y boton")
boton = tk.Button(ventana, text="Haz clic aqui", command=saludar)
boton.pack()
ventana.mainloop()

## metodos http
## GET: obtener informacion
## post: enviar informacion json




