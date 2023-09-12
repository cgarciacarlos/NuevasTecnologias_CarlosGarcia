registro = []
bicicletas = ["bicicletaVerde", "bicicletaBlanca", "bicicletaAzul"]

def Registro_usuario ():
    nombre = input ("Ingrese nombre: ")
    apellido = input ("Ingrese Apellido")
    correo = input ("Ingrese correo")
    numeroTarjeta = input ("Ingrese numero tarjeta")
    nuevoDato = {"nombre":nombre, "apellido":apellido, "correo":correo, "numeroTarjeta":numeroTarjeta}

    registro.append(nuevoDato)
    print("Nuevo Usuario",nombre, "Registrado correctamente")

def Reserva_Bicicleta():
    numeroTarjeta = input("Ingrese su numero de tarjeta: ")
    usuario_Encontrado = None
    for nuevoDato in registro:
         if nuevoDato["tarjeta"] == numeroTarjeta:
            usuario_Encontrado = nuevoDato

            for nuevoDato in registro:
                if nuevoDato["tarjeta"] == numeroTarjeta:
                    usuario_Encontrado = nuevoDato
                break
            if  usuario_Encontrado:
                if bicicletas:
                 origen = input("Ingrese el origen de la bicicleta: ")
                 destino = input("Ingrese el destino de la bicicleta: ")
                 bicicletas = bicicletas.pop()
                print(f"{usuario_Encontrado['nombre']} se le asigno la cicla{bicicletas} desde{origen} hacia{destino}")

            else:
                print("No Hay bicicletas en este momento")
    else:
        print("Usuario no registrado")

    while True:
        print("1. Registrar Usuario")
        print("2. Prestar bicicleta")
        print("3. salir")

        opcion = input("Escoja una opcion: ")

        if opcion == "1":
            Registro_usuario()
        elif opcion == "2":
            Reserva_Bicicleta()
        elif opcion == "3":
            print("Gracias por utilizar los servicios")



        else:
            print("Error verifica la opcion")

