class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    # getter
    @property
    def nome(self):
        print('chamando @property nome()')
        return self.__nome.title()

    # setter
    @nome.setter
    def nome(self, nome):
        print('chamando setter nome()')
        self.__nome = nome

cliente = Cliente('aline')
cliente.nome = 'gui'
print(cliente.nome)
