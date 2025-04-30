class Funcionario():
    def __init__(self, nome, id_funcionario, salario_base,):
        self.__nome = nome        
        self.__id_funcionario = id_funcionario
        self.__salario_base = salario_base
        self.__bonus = 0
        self.__faltas = 0
    
    def registrar_falta(self):
        self.__faltas+=1

    def adicionar_bonus(self, bonus):
        self.__bonus+=bonus

    def recalcular_bonus(self):
        return self.__bonus
    
    def get_id(self):
        return self.__id_funcionario
    
    def cacular_salario(self):
        return self.__salario_base
    
    def resumo(self):
        return f"O funcionario {self.__nome}\nTem o salario de R${self.__salario_base} com o bonus de R${self.__bonus}\nFaltou {self.__faltas} vezes"