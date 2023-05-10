import sys, os
sys.path.append(os.getcwd())

from codigo.calculadora import Calculator

class TestCalculator:
    def test_divisao_de_dois_valores_positivos(self):
        numero_a = 2
        numero_b = 5
        resultado_esperado = 0.4

        resultado = Calculator().division(numero_a, numero_b)
        
        assert resultado_esperado == resultado

    def test_divisao_de_dois_valores_negativos(self):
        numero_a = -4
        numero_b = -3
        resultado_esperado = 1.33

        resultado = Calculator().division(numero_a, numero_b)
        
        assert resultado_esperado == resultado

    def test_divisao_de_dois_valores_invalidos(self):
        numero_a = 'olá'
        numero_b = 'teste'
        resultado_esperado = None

        resultado = Calculator().division(numero_a, numero_b)
        
        assert resultado_esperado == resultado

    def test_divisao_de_dois_valores_decimais(self):
        numero_a = 2.5
        numero_b = 1.5
        resultado_esperado = 1.67

        resultado = Calculator().division(numero_a, numero_b)
        
        assert resultado_esperado == resultado

    def test_divisao_por_zero(self):
        numero_a = 1
        numero_b = 0
        resultado_esperado = 0

        resultado = Calculator().division(numero_a, numero_b)
        
        assert resultado_esperado == resultado