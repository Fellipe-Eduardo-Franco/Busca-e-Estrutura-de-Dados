import unittest
from busca import busca_linear

class TestBuscaLinear(unittest.TestCase):

    def test_valor_existente(self):
        self.assertEqual(
            busca_linear([10, 20, 30, 40], 30),
            2
        )

    def test_valor_inexistente(self):
        self.assertEqual(
            busca_linear([10, 20, 30, 40], 50),
            -1
        )

if __name__ == "__main__":
    unittest.main()
