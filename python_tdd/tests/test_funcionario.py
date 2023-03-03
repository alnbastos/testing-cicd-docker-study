from funcionario import Funcionario

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

