import unittest
from SRC.calculos_estadisticos import CalculosEstadisticos

class TestCalculosEstadisticos(unittest.TestCase):
    def setUp(self):
        self.calculos = CalculosEstadisticos()

    def tearDown(self):
        self.calculos = None
    def test_calcular_media(self):
        # Arrange
        numero = [1, 2, 3, 4, 5]
        resultado_esperado = 3.0
        # Do
        resultado_actual = self.calculos.calcular_media(numero)
        # Assert
        self.assertEqual(resultado_esperado, resultado_actual)
        # Caso adicional
        numero = [10, 20, 30, 40, 50]
        resultado_esperado = 30.0
        resultado_actual = self.calculos.calcular_media(numero)
        self.assertEqual(resultado_esperado, resultado_actual)
    def test_calcular_desviacion_estandar(self):
        # Arrange
        numero = [1, 2, 3, 4, 5]
        resultado_esperado = 1.58
        # Do
        resultado_actual = self.calculos.calcular_desviacion_estandar(numero)
        # Assert
        self.assertAlmostEqual(resultado_esperado, resultado_actual, places=2)
        # Casos adicionales
        numero = [10, 20, 30, 40, 50]
        resultado_esperado = 15.81
        resultado_actual = self.calculos.calcular_desviacion_estandar(numero)
        self.assertAlmostEqual(resultado_esperado, resultado_actual, places=2)
        # Caso para lista vacía
        numero = []
        resultado_actual = self.calculos.calcular_desviacion_estandar(numero)
        self.assertIsNone(resultado_actual)
if __name__ == '__main__':
    unittest.main()

