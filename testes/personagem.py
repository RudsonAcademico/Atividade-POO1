class Personagem():
    def __init__(self, nome, classe):
        self.nome = nome
        self.__classe = classe
        self.__nivel = 0
        self.__experiencia = 0
        self.vida = 100
        self.__forca = 10
        self.__inventario = []

    def calcular_vida_base(self):
        return self.vida

    def calcular_forca_base(self):
        return self.__forca
    
    def atacar(self):
        return self.__forca

    def receber_dano(self, dano):
        self.vida -= dano
        return self.vida

    def ganhar_experiencia(self, xp):
        self.__experiencia+=xp

    def verificar_nivel(self):
        return self.__nivel

    def adicionar_item(self, item):
        self.__inventario.append(item)

    def status(self):
        return f"O {self.__classe} {self.nome}\nEsta no Nivel {self.__nivel} com {self.__experiencia} pontos de experiencia"
