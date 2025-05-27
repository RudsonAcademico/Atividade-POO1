class Funcionario():
    empresa = "Tech Solutions"
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @classmethod
    def alterar_nome_empresa(cls, nome):
        cls.empresa = nome

    @staticmethod
    def boas_vindas():
        print("Bem-Vindo à empresa!")



joao = Funcionario("João", 1000)
print(joao.empresa)
Funcionario.alterar_nome_empresa("Nova Tech")

pedro = Funcionario("Pedro", 1000)

print(joao.empresa)

Funcionario.boas_vindas()