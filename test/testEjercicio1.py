import unittest
from ejercicio1 import Inventario

class TestInventario(unittest.TestCase):
    def setUp(self):
        """Inicializa un inventario nuevo para cada prueba."""
        self.inventario = Inventario()

    def test_añadir_y_obtener_producto(self):
        self.inventario.añadir_producto("Laptop", 10, 1500.00)
        producto = self.inventario.obtener_producto("Laptop")
        self.assertEqual(producto, {"nombre": "Laptop", "cantidad": 10, "precio": 1500.00})

    def test_actualizar_producto(self):
        self.inventario.añadir_producto("Laptop", 10, 1500.00)
        self.inventario.actualizar_producto("Laptop", cantidad=15, precio=1400.00)
        producto = self.inventario.obtener_producto("Laptop")
        self.assertEqual(producto, {"nombre": "Laptop", "cantidad": 15, "precio": 1400.00})

    def test_eliminar_producto(self):
        self.inventario.añadir_producto("Laptop", 10, 1500.00)
        self.inventario.eliminar_producto("Laptop")
        self.assertRaises(KeyError, self.inventario.obtener_producto, "Laptop")

    def test_listar_productos(self):
        self.inventario.añadir_producto("Laptop", 10, 1500.00)
        self.inventario.añadir_producto("Mouse", 50, 25.00)
        productos = self.inventario.listar_productos()
        self.assertEqual(len(productos), 2)

if __name__ == '__main__':
    unittest.main()
