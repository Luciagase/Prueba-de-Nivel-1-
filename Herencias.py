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
    


"""def catalogar(lista):
    for vehiculo in lista:
        print("{}".format(type(vehiculo).__name__)) 
        #print(type(vehiculo).__name__) 
        print(vehiculo, "\n")"""

def catalogar(lista,ruedas=None):

    if ruedas != None:
        contador = 0
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                contador += 1
        print("Se han encontrado {} vehiculos con {} ruedas: ".format(contador,ruedas))
        

    for vehiculo in lista:
        if ruedas == None:
            print("{} {}".format(type(vehiculo).__name__, vehiculo))
        else:
            if vehiculo.ruedas == ruedas:
                print("{} {}".format(type(vehiculo).__name__,vehiculo))


coche = Coche("rosa",4,240,650)
camion = Camioneta("azul",6,170,800,5000)
bici = Bicicleta("rojo",2,"urbana")
moto = Motocicleta("gris",2,"urbana",195,350)
coche1 = Coche("negro",4,200,640)
camion1 = Camioneta("blanco",6,200,600,1000)
bici1 = Bicicleta("marrón",2,"deportiva")
moto1 = Motocicleta("gris",2,"urbana",180,250)
coche2 = Coche("blanco",4,130,700)
camion2 = Camioneta("gris",6,120,800,3000)
bici2 = Bicicleta("azul",2,"urbana")
moto2 = Motocicleta("negro",2,"deportiva",195,350)

# Lista
vehiculos = [coche, camion, bici, moto, coche1, camion1, bici1, moto1, coche2, camion2, bici2, moto2]

catalogar(vehiculos,2)