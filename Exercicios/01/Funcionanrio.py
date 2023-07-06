class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def add_aumento(self, valor):
        self.__salario += valor

    def ganho_anual(self):
        return self.__salario * 12

    def exibe_dados(self):
        print("Nome:", self.nome)
        print("Salário:", self.salario)