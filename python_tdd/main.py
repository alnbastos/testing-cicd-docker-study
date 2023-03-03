from funcionario import Funcionario

# aline = Funcionario('Aline', '03/12/1998', 1_000)
# print(aline.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '03/12/1998', 1_111)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()