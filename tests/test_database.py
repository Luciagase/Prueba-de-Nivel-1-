import csv
import copy
import config
import helpers
import unittest
import batabase as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Vehiculos.lista = [
            db.Vehiculo('KJ4', 'rosa', 4),
            db.Vehiculo('RF3', 'gris', 6),
            db.Vehiculo('IU6', 'marrón', 2)
        ]

    def test_buscar_vehiculo(self):
        vehiculo_existente = db.Vehiculos.buscar('KJ4')
        vehiculo_inexistente = db.Vehiculos.buscar('XX3')
        self.assertIsNotNone(vehiculo_existente)
        self.assertIsNone(vehiculo_inexistente)

    def test_bastidor_valido(self):
        self.assertTrue(helpers.bastidor_valido('GS5', db.Vehiculos.lista))
        self.assertFalse(helpers.bastidor_valido('232323S', db.Vehiculos.lista))
        self.assertFalse(helpers.bastidor_valido('F35', db.Vehiculos.lista))
        self.assertFalse(helpers.bastidor_valido('HGH', db.Vehiculos.lista))

