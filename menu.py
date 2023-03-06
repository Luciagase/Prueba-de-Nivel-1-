# La interfaz que mostrará por la terminal un menú
import helpers
import database as db


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("===============================================")
        print("       Bienvenido al Gestor de vehículos       ")
        print("===============================================")
        print("[1]         Listar los vehículos               ")
        print("[2]       Buscar vehículo por bastidor         ")
        print("[3]       Buscar vehículos por ruedas          ")
        print("[4]           Cerrar el Gestor                 ")
        print("===============================================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los vehículos...\n")
            for vehiculo in db.Vehiculos.lista:
                print(vehiculo)

        elif opcion == '2':
            print("Buscando vehiculo...\n")
            bastidor = helpers.leer_texto(3, 3, "Ruedas (2 char y 1 int)").upper()
            vehiculo = db.Vehiculos.buscar(bastidor)
            print(vehiculo) if vehiculo else print("Vehiculo no encontrado.")

        elif opcion == '3':
            print("Buscando vehiculos...\n")
            ruedas = helpers.leer_numero(2, 4, 6, "Ruedas (2, 4, 6)")
            db.Vehiculos.catalogar(ruedas)
        

        elif opcion == '4':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")