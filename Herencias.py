class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__(self) + ", {}".format(self.tipo)
    
class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    

class Camioneta(Coche):
    
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + ", {} kg".format(self.carga)
    

coche = Coche("rosa",4,240,650)
camion = Camioneta("azul",6,170,800,5000)
bici = Bicicleta("rojo",2,"urbana")
moto = Motocicleta("gris",2,"urbana",195,350)

# Lista
vehiculos = [coche, camion, bici, moto]