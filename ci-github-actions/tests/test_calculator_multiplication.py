import sys, os
sys.path.append(os.getcwd())

from codigo.calculadora import Calculator

class TestCalculator:
    def test_multiplicacao_de_dois_valores_positivos(self):
        numero_a = 2
        numero_b = 5
        resultado_esperado = 10

        resultado = Calculator().multiplication(numero_a, numero_b)
        
        assert resultado_esperado == resultado

    def test_multiplicacao_de_dois_valores_negativos(self):
        numero_a = -1
        numero_b = -20
        resultado_esperado = 20

        resultado = Calculator().multiplication(numero_a, numero_b)
        
        assert resultado_esperado == resultado

    def test_multiplicacao_de_dois_valores_invalidos(self):
        numero_a = 'olá'
        numero_b = 'teste'
        resultado_esperado = None

        resultado = Calculator().multiplication(numero_a, numero_b)
        
        assert resultado_esperado == resultado

    def test_multiplicacao_de_dois_valores_decimais(self):
        numero_a = 2.5
        numero_b = 1.5
        resultado_esperado = 3.75

        resultado = Calculator().multiplication(numero_a, numero_b)
        
        assert resultado_esperado == resultado