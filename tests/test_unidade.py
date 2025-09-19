import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.calculadora import Calculadora

class test_unidade(unittest.TestCase):
    
    # testes de operacao
    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)
        
    def test_entrada_saida_subtracao(self):
        calc = Calculadora()
        resultado = calc.subtrair(5, 3)
        self.assertEqual(resultado, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 2)
        
    def test_entrada_saida_multiplicacao(self):
        calc = Calculadora()
        resultado = calc.multiplicar(5, 3)
        self.assertEqual(resultado, 15)
        self.assertEqual(calc.obter_ultimo_resultado(), 15)
        
    def test_entrada_saida_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(6, 3)
        self.assertEqual(resultado, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 2)
        
    def test_entrada_saida_potencia(self):
        calc = Calculadora()
        resultado = calc.potencia(3, 3)
        self.assertEqual(resultado, 27)
        self.assertEqual(calc.obter_ultimo_resultado(), 27)
    
        
    #Teste de tipagem invalida
    def test_tipagem_invalida(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3) # String no lugar de numero
        with self.assertRaises(TypeError):
            calc.subtrair(1, "2") 
        with self.assertRaises(TypeError):
            calc.multiplicar(None, 2)
        with self.assertRaises(TypeError):
            calc.dividir(10, None) # None no lugar de numero
        with self.assertRaises(TypeError):
            calc.potencia("2", 3)
            
    # teste de consistencia
    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)

    # teste de inicializacao
    
    #teste de modificacao de dados
    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
        
    # Testar comportamento com valores minimos
    def test_limite_inferior(self):
        calc = Calculadora()
         # Teste com zero
        resultado = calc.somar(0, 5)
        self.assertEqual(resultado, 5)
         # Teste com numeros negativos muito pequenos
        resultado = calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado, -2e-10)
    
    #Teste com numeros grandes
    def test_limite_superior(self):
        calc = Calculadora()
        resultado = calc.somar(1e300, 1e300)
        self.assertEqual(resultado, 2e300)
        
    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)
            
    def test_fluxos_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)
        
        
    def test_mensagens_erro(self):
        calc = Calculadora()
        try:
            calc.dividir(5, 0)
        except ValueError as e:
            self.assertEqual(str(e), "Divisao por zero nao permitida")



if __name__ == '__main__':
    unittest.main()

