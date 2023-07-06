from Funcionanrio import Funcionario

class Assistente(Funcionario):
    def __init__(self, nome, salario, numero_matricula):
        super().__init__(nome, salario)
        self.__numero_matricula = numero_matricula

    def exibe_dados(self):
        super().exibe_dados()
        print("Número de Matrícula:", self.numero_matricula)
