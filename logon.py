usuarios = {"admin": "123"}

def iniciar_sesion():
    while True:
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if usuario in usuarios and usuarios[usuario] == contrasena:
            print("Inicio de sesión exitoso. ¡Bienvenido,", usuario, "!")
            break
        else:
            print("Nombre de usuario o contraseña incorrectos. Intente de nuevo.")

if __name__ == "__main__":
    print("inicio de sesión")
    iniciar_sesion()
