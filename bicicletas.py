class SistemaPrestamoBicicletas:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, apellido, correo, numero_bicicleta, numero_tarjeta):
        nuevo_usuario = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Correo": correo,
        "Numero de Bicicleta": numero_bicicleta,
        "Numero de Tarjeta": numero_tarjeta,
        }
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario {nombre} registrado con éxito.")

    def mostrar_usuarios(self):
        print("\nLista de Usuarios:")
        for usuario in self.usuarios:
            print(f"Nombre: {usuario['Nombre']},Apellido: {usuario['Apellido']}, Correo: {usuario['correo']},Numero de Bicicleta: {usuario['numero_bicicleta']},Numero de Tarjeta: {usuario['numero_tarjeta']}")


def main():
    sistema = SistemaPrestamoBicicletas()

    while True:
        print("\nSistema de Préstamo de Bicicletas")
        print("1. Registrar Usuario")
        print("2. Mostrar Usuarios")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            apellido = input("Ingrese el apellido: ")
            correo = input("Ingrese el correo: ")
            numero_bicicleta = int (input("Ingrese numero de bicicleta: "))
            numero_tarjeta = int (input("Ingrese el número de tarjeta del usuario: "))
            sistema.registrar_usuario(nombre,apellido, correo, numero_bicicleta, numero_tarjeta)
        elif opcion == "2":
            sistema.mostrar_usuarios()
        elif opcion == "3":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
