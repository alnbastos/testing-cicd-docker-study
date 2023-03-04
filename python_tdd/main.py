from funcionario import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Teste', '03/12/1998', 1_111)
    print(f'Teste = {funcionario_teste.idade()}')


def teste_calcular_bonus():
    ana = Funcionario('Ana', '12/03/1997', 100_000)
    print(ana.calcular_bonus())


if __name__ == '__main__':
    teste_idade()
    teste_calcular_bonus()
