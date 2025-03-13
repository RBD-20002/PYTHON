def login_usuario():
    global usuario , contraseña
    usuario = input("Introduce usuario: ")
    contraseña = input("Introduce contraseña: ")
    repite_contraseña = input("Repite tu contraseña: ")
    while contraseña != repite_contraseña:
        print("La contraseña no coincide")
        contraseña = input("Introduce contraseña: ")
        repite_contraseña = input("Repite tu contraseña: ")
    print("Usuario registrado")

def validar_usuario():
    usuario_input = input("Introduce usuario: ")
    contraseña_input = input("Introduce contraseña: ")
    while usuario_input != usuario or contraseña_input != contraseña:
        print("El usuario o la contraseña no coincede")
        usuario_input = input("Introduce usuario: ")
        contraseña_input = input("Introduce contraseña: ")
    print("Bienvenido")

login_usuario()
validar_usuario()