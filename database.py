#Encargado de manejar la gestión de los datos
import csv
import config


class Vehiculo:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"

    def to_dict(self):
        return {'dni': self.dni, 'nombre': self.nombre, 'apellido': self.apellido}


class Clientes:

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido in reader:
            vehiculo = Vehiculo(dni, nombre, apellido)
            lista.append(vehiculo)

    @staticmethod
    def buscar(dni):
        for vehiculo in Clientes.lista:
            if vehiculo.dni == dni:
                return vehiculo
