# tests/test_integracao.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.calculadora import Calculadora

class test_integracao(unittest.TestCase):
    def test_operacoes_sequenciais(self):
        calc = Calculadora()
        calc.somar(2, 3)                      # 5
        resultado1 = calc.obter_ultimo_resultado()
        calc.multiplicar(resultado1, 4)      # 20
        resultado2 = calc.obter_ultimo_resultado()
        calc.dividir(resultado2, 2)          # 10
        resultado_final = calc.obter_ultimo_resultado()
        self.assertEqual(resultado_final, 10)
        self.assertEqual(len(calc.historico), 3)

    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        calc.potencia(2, 3)                  # 8
        calc.somar(calc.obter_ultimo_resultado(), 2)  # 10
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)

    # Teste extra: sequência com limpar_historico no meio
    def test_sequencia_com_limpar(self):
        calc = Calculadora()
        calc.somar(1, 2)    # histórico 1
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
        calc.multiplicar(3, 3)
        self.assertEqual(calc.obter_ultimo_resultado(), 9)
        self.assertEqual(len(calc.historico), 1)

if __name__ == "__main__":
    unittest.main()
