usuario = "Alexander".lower().strip()
contraseña = "R2068AML".strip()

usuariopers = input("Ingrese un usuario: ").lower().strip()
contaseñapers = input("Ingrese una contraseña: ").strip()

if usuario == usuariopers and contraseña == contaseñapers:
    print("Acceso permitido")
else:
    print("Acceso denegado")



