class Data:
    def __init__(self, dia, mes, ano):
        if (1 <= dia <= 31) and (1 <= mes <= 12):
            self.dia = dia
            self.mes = mes
            self.ano = ano
            self.valido = True
        else:
            self.valido = False

    def formatada(self):
        if self.valido:
            print(f'{self.dia}/{self.mes}/{self.ano}')
        else:
            print('Data incorreta')

d = Data(1, 11, 2007)
d.formatada()
