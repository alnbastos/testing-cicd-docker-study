class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__condigo_banco = '001'

    def extrato(self):
        print(f'O Titular {self.__titular} tem um Saldo de {self.__saldo}')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print('Saque efetuado.')
        else:
            print(f'O valor {valor} passou o limite de saque.')

    # encapsulamento
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print(f'Foi transferido um valor de R${valor} do titular {self.__titular} para {destino.__titular}')

    # getters e setters
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Métodos da classe
    @staticmethod
    def codigo_banco():
        return '001'

    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


conta = Conta(123, 'Aline', 55, 1000)
conta2 = Conta(345, 'Gui', 100, 1000)

conta._Conta__saldo # atributo não acessavel, apenas uso dentro da classe
print()
conta.extrato()
conta.deposita(100)
conta.saca(10)
conta.extrato()
print()

conta2.extrato()

print()
conta.transfere(10, conta2)

print()
print('Utilizando Getters e Setters:')
print(f'Titular: {conta.titular} | Saldo: {conta.saldo} | Limite: {conta.limite}')
conta.limite = 2000
print(f'Titular: {conta.titular} | Saldo: {conta.saldo} | Limite: {conta.limite}')

print()
print('Métodos privados:')
conta.saca(2500)

print()
print('Métodos de classe:')
print(Conta.codigos_bancos())