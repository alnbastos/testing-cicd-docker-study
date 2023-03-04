from funcionario import Funcionario
import pytest

# O nome do método deve sempre começar com test_, seguido com a descrição verbosa
class TestFuncionario:
    def test_quando_idade_recebe_13_07_1998_deve_retornar_25(self):
        # GIVEN (Contexto)
        data_entrada = '13/07/1998'
        idade_esperada = 25
        funcionario_teste = Funcionario('Teste', data_entrada, 1_000)
        
        # WHEN (Ação)
        idade_resultado = funcionario_teste.idade()

        # THEN (Desfecho)
        assert idade_resultado == idade_esperada

    def test_quando_sobrenome_recebe_Aline_Bastos_deve_retornar_apenas_Bastos(self):
        # GIVEN (Contexto)
        nome_entrada = ' Aline Bastos'
        sobrenome_esperado = 'Bastos'
        aline = Funcionario(nome_entrada, '13/07/1998', 1_000)

        # WHEN (Ação)
        sobrenome_resultado = aline.sobrenome()

        # THEN (Desfecho)
        assert sobrenome_resultado == sobrenome_esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        # GIVEN (Contexto)
        salario_entrada = 100_000
        nome_entrada = 'Paulo Bragança'
        
        salario_esperado = 90_000

        funcionario_teste = Funcionario(nome_entrada, '13/07/1998', salario_entrada)

        # WHEN (Ação)
        funcionario_teste.decrescimo_salario()
        salario_resultado = funcionario_teste.salario

        # THEN (Desfecho)
        assert salario_resultado == salario_esperado

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # GIVEN (Contexto)
        salario_entrada = 1_000
        salario_esperado = 100

        funcionario_teste = Funcionario('Teste', '13/07/1998', salario_entrada)

        # WHEN (Ação)
        salario_resultado = funcionario_teste.calcular_bonus()

        # THEN (Desfecho)
        assert salario_resultado == salario_esperado
    
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            # GIVEN (Contexto)
            salario_entrada = 1_000_000

            funcionario_teste = Funcionario('Teste', '13/07/1998', salario_entrada)

            # WHEN (Ação)
            salario_resultado = funcionario_teste.calcular_bonus()

            # THEN (Desfecho)
            assert salario_resultado

    