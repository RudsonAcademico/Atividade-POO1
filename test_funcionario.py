from funcionario import Funcionario

# Criando funcionários
departamento = []
func1 = Funcionario("Ana Silva", "F001", 3000)
departamento.append(func1)

# Realizando operações
func1.adicionar_bonus(500)
print(func1.resumo())

func1.registrar_falta()
func1.registrar_falta()
print(func1.resumo())
