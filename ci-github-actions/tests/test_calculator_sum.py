import sys, os
sys.path.append(os.getcwd())

from codigo.calculadora import Calculator

class TestCalculator:
    def test_soma_de_dois_valores_positivos(self):
        numero_a = 1
        numero_b = 1
        resultado_esperado = 2

        resultado = Calculator().sum(numero_a, numero_b)
        
        assert resultado_esperado == resultado

    def test_soma_de_dois_valores_negativos(self):
        numero_a = -1
        numero_b = -1
        resultado_esperado = -2

        resultado = Calculator().sum(numero_a, numero_b)
        
        assert resultado_esperado == resultado

    def test_soma_de_dois_valores_invalidos(self):
        numero_a = 'olá'
        numero_b = 'teste'
        resultado_esperado = None

        resultado = Calculator().sum(numero_a, numero_b)
        
        assert resultado_esperado == resultado

    def test_soma_de_dois_valores_decimais(self):
        numero_a = 1.5
        numero_b = 2.5
        resultado_esperado = 4

        resultado = Calculator().sum(numero_a, numero_b)
        
        assert resultado_esperado == resultado