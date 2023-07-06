from Assistente import Assistente

class Administrativo(Assistente):
    def __init__(self, nome, salario, numero_matricula, turno, adicional_noturno):
        super().__init__(nome, salario, numero_matricula)
        self.__turno = turno
        self.__adicional_noturno = adicional_noturno

    def ganho_anual(self):
        salario_anual = self.__salario * 12
        if self.__turno.lower() == "noite":
            salario_anual += self.__adicional_noturno * 12
        return salario_anual