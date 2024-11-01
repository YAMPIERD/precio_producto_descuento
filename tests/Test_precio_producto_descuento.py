import unittest
from src.logica.precio_producto_descuento import PrecioProductoDescuento
class TestPrecioProductoDescuento(unittest.TestCase):
    def test_descuento_normal(self):
        self.assertAlmostEqual(PrecioProductoDescuento.calcular_precio_final(100, 10), 90.0)

    def test_sin_descuento(self):
        self.assertAlmostEqual(PrecioProductoDescuento.calcular_precio_final(100, 0), 100.0)

    def test_descuento_completo(self):
        self.assertAlmostEqual(PrecioProductoDescuento.calcular_precio_final(100, 100), 0.0)

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
            PrecioProductoDescuento.calcular_precio_final(-100, 10)

    def test_descuento_negativo(self):
        with self.assertRaises(ValueError):
            PrecioProductoDescuento.calcular_precio_final(100, -10)

    def test_precio_no_numerico(self):
        with self.assertRaises(TypeError):
            PrecioProductoDescuento.calcular_precio_final("cien", 10)

    def test_descuento_no_numerico(self):
        with self.assertRaises(TypeError):
            PrecioProductoDescuento.calcular_precio_final(100, "diez")


if __name__ == '__main__':
    unittest.main()
