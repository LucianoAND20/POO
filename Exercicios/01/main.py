from Funcionanrio import Funcionario
from Assistente import Assistente
from Tecnico import Tecnico
from Administrativo import Administrativo

fun = Funcionario("João", 2000.0)
fun.add_aumento(500.0)
fun.exibe_dados()
print("Ganho anual:", fun.ganho_anual())

ast = Assistente("Maria", 1500.0, 12345)
ast.add_aumento(300.0)
ast.exibe_dados()
print("Ganho anual:", ast.ganho_anual())

tec = Tecnico("Pedro", 2500.0, 54321, 1000.0)
tec.add_aumento(400.0)
tec.exibe_dados()
print("Ganho anual:", tec.ganho_anual())

adm = Administrativo("Ana", 1800.0, 67890, "noite", 200.0)
adm.add_aumento(200.0)
adm.exibe_dados()
print("Ganho anual:", adm.ganho_anual())
