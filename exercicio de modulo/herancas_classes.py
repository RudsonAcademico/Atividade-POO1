class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")

    def calcular_bonus(self):
        return self.salario * 0.05



class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Departamento: {self.departamento}")

funciona = Funcionario("Mamede", 4444)

generente = Gerente("Marmama", 19053135, "Cacino")


funciona.mostrar_informacoes()
print()
generente.mostrar_informacoes()