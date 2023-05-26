class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Space(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Spacer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Kadima(Funcionario):
    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Geek:
    def __str__(self):
        return f'Geeker,  {self.nome}'

class Junior(Kadima):
    pass

class Pleno(Kadima, Space, Geek):
    pass


andre = Junior('André')
andre.busca_perguntas_sem_resposta()
andre.mostrar_tarefas()

renan = Pleno('Renan')
renan.busca_perguntas_sem_resposta()
renan.busca_cursos_do_mes()

renan.mostrar_tarefas()

print(renan)