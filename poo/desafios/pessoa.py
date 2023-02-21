"""
Link que contem o exercício: https://wiki.python.org.br/ExerciciosClasses

Desafio: 
Crie uma classe Pessoa que modele uma pessoa:
    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer.

Obs: Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm. 
"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def envelhecer(self, ano:int) -> None:
        self.__idade += ano
        for _ in range(ano):
            self.crescer()

    def engordar(self, valor:float) -> None:
        self.__peso += valor

    def emagrecer(self, valor:float) -> None:
        self.__peso -= valor

    def crescer(self, altura:float=0.5) -> None:
        self.__altura += altura

    def exibir_pessoa(self):
        print(f'Nome: {self.__nome} | Idade: {self.__idade} | Peso: {self.__peso} | Altura: {self.__altura:.2f}')


pessoa = Pessoa('Aline', 24, 53, 1.61)

pessoa.engordar(2.50)
pessoa.emagrecer(2)

pessoa.envelhecer(2)
pessoa.crescer(2)

pessoa.exibir_pessoa()
