import unittest
from src.analise_dados import calcular_estatisticas
import pandas as pd

class TestAnaliseDados(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Produto': ['A', 'B', 'C'],
            'Categoria': ['X', 'Y', 'Z'],
            'Preço': [10, 20, 30],
            'Quantidade': [1, 2, 3]
        })

    def test_calcular_estatisticas(self):
        media, mediana, desvio = calcular_estatisticas(self.df)
        self.assertAlmostEqual(media, 20)
        self.assertAlmostEqual(mediana, 20)
        self.assertAlmostEqual(desvio, 1)

if __name__ == '__main__':
    unittest.main()
