class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__idade = 0
    
    @property
    def idade(self):
        return self.__idade

    @property
    def nome(self):
        return self.__nome
    
    @idade.setter
    def idade(self, idade):
        if idade < 0:
            print("Idade invalida")
            self.__idade = 0
        else:
            self.__idade = idade

    @nome.setter
    def nome(self, nome):
        if not nome or nome == " ":
            print("Valor invalido pra nome")
            self.__nome = "Enzo"
        else:
            self.__nome = nome


person = Pessoa()


person.nome = "Pedro"
person.idade = 23

print(f"{person.nome} tem {person.idade} anos")