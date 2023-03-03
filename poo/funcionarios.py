class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostra_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Caelumer!')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum.')


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


jose = Junior()
jose.busca_perguntas_sem_resposta()
# jose.busca_cursos_do_mes() # Não funciona pois não está sendo herdado

luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostra_tarefas()
