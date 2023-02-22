"""
Link que contem o exercício: https://wiki.python.org.br/ExerciciosClasses

Desafio:
Crie uma classe Bichinho Virtual que modele um Tamagotchi (Bichinho Eletrônico):
    Atributos: Nome, Fome, Saúde e Idade.
    Métodos: Alterar Nome, Fome, Saúde e Idade;
    Retornar: Nome, Fome, Saúde e Idade.
    
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagotchi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento. 
"""

class Tamagotchi:
    def __init__(self, nome, fome, saude, idade) -> None:
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade

    def alterar_nome(self, novo_nome) -> None:
        self.__nome = novo_nome.title()

    def fome(self, valor) -> None:
        self.__validar(valor, self.__fome, "Fome")

    def saude(self, valor) -> None:
        self.__validar(valor, self.__saude, "Saúde")

    def idade(self, valor) -> None:
        self.__idade += valor

    def exibir_tamagotchi(self) -> None:
        print(f'Nome: {self.__nome} | Fome: {self.__fome} | Saúde: {self.__saude} | Idade: {self.__idade} | Humor: {self.__humor()}')
    
    # @property.setter
    def __humor(self) -> float:
        return (self.__fome + self.__saude)/2

    def __validar(self, valor, atributo, tipo_mensagem):
        if valor < 11:
            if atributo < 10:
                atributo += valor
            else:
                print(f'{self.__nome} já possui {atributo} de {tipo_mensagem}.')
        else:
            print(f'{tipo_mensagem} - Insira um valor de até 10.')


tamagotchi = Tamagotchi('Jeremias', 10, 10, 1)

tamagotchi.alterar_nome('Alfred')
tamagotchi.fome(2)
tamagotchi.saude(1)
tamagotchi.idade(2)

tamagotchi.exibir_tamagotchi()
