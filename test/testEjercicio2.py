import unittest
from src.ejercicio2 import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calculadora.sumar(3, 2), 5)
        self.assertEqual(self.calculadora.sumar(-1, 1), 0)
        self.assertEqual(self.calculadora.sumar(0, 0), 0)

    def test_restar(self):
        self.assertEqual(self.calculadora.restar(3, 2), 1)
        self.assertEqual(self.calculadora.restar(-1, 1), -2)
        self.assertEqual(self.calculadora.restar(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(self.calculadora.multiplicar(3, 2), 6)
        self.assertEqual(self.calculadora.multiplicar(-1, 1), -1)
        self.assertEqual(self.calculadora.multiplicar(0, 5), 0)

    def test_dividir(self):
        self.assertEqual(self.calculadora.dividir(4, 2), 2)
        self.assertEqual(self.calculadora.dividir(5, 2), 2.5)
        self.assertEqual(self.calculadora.dividir(-1, 1), -1)
        self.assertEqual(self.calculadora.dividir(0, 5), 0)
        self.assertEqual(self.calculadora.dividir(5, 0), "Error: No se puede dividir entre cero.")

if __name__ == '__main__':
    unittest.main()
