from Assistente import Assistente

class Tecnico(Assistente):
    def __init__(self, nome, salario, numero_matricula, bonus_salarial):
        super().__init__(nome, salario, numero_matricula)
        self.__bonus_salarial = bonus_salarial

    def ganho_anual(self):
        return (self.__salario + self.__bonus_salarial) * 12