import random

#criação de classes
#continuação do capitulo 2

class Jogo:
    def __init__(self):
        self.__dificuldade = 2

    
    @property
    def dificuldade(self):
        return self.__dificuldade
    
    @dificuldade.setter
    def dificuldade(self,valor):
        if valor >= 1 and valor <= 3:
            self.__dificuldade = valor
        

    def iniciar(self):
        print("O jogo começou!")
    
    def pular(self):
        print("O personagem pulou!")


class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.__forca = forca

    
    def definir_vida(self, quantidade):
        self.vida = quantidade

    @property
    def atacar(self):
        print(self.__forca)

    

class Pontuacao():
    def __init__(self):
        self.__pontos = 0

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self,valor):
        if valor >= 0:
            self.__pontos+=valor
            print(self.pontos())
        else:
            print("Valor invalido")

    def zerar_pontos(self):
        self.__pontos = 0
        print("Pontuação zerada!")
    

class Personagem:
    def __init__(self, vida, nome):
        self.__vida = vida
        self.nome = nome
        self.__defesa = 50

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self,valor):
        if valor <= 100 and valor >= 0:
            self.__defesa = valor
    
    def dizer_nome(self):
        print(f"Meu nome é {self.nome}")

    def tomar_dano(self, dano):
        self.__vida-=dano
        if self.__vida <= 0:
            print("Game Over!") 
            

    def fim_de_jogo(self):
        print("Game Over!")
    
    @property
    def mostrar_vida(self):
        return self.__vida
    

class Jogador():
    def __init__(self, nome, energia, pontos):
        self.__energia = energia
        self.nome = nome
        self.pontos = pontos
    
    def recuperar_energia(self, valor):
        self.__energia += valor
        if self.__energia > 100:
            print("você esta com energia maxima")
            self.__energia = 100
        else:
            print(f"Você recuperou {valor} pontos de energia")
    
    def usar_energia(self, valor):
        self.__energia -= valor
        if self.__energia <= 0:
            print("Sem energia suficiente!")

    def atacar(self, alvo, valor):
        print(f"Você atacou! e causou {valor} de dano")
        alvo.vida-=valor
        self.usar_energia(10)

class Menu:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def iniciar_jogo(self, game):
        game.iniciar()
    
    def mostrar_opcoes(self):
        print("Modos de Jogo:\n1: Facil\n2: Médio\n3: Dificil")
    
    def sair(self):
        print("O Jogo foi Fechado")
    
#classe hedeiras

class NPC(Personagem):
    def __init__(self, vida, nome, defesa):
        super().__init__(vida, nome, defesa)

class Chefe(Inimigo):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida * 2, forca * 2)

class JogadorPremium(Jogador):
    def __init__(self, nome, energia, pontos):
        super().__init__(nome, energia, pontos)




#chamados de metodos de classes
game = Jogo()

pontos = Pontuacao()

menu = Menu()

player = Jogador()

mob = Personagem()

bixo = Inimigo()
