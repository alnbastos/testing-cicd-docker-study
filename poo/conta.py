class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O Titular {self.__titular} tem um Saldo de {self.__saldo}')

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    # encapsulamento
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print(f'Foi transferido um valor de R${valor} do titular {self.__titular} para {destino.__titular}')

    def inadimplemente(self):
        pass

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