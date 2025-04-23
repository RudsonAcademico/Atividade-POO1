import random

#criação de classes

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
            self.mostrar_pontos()
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
    

class Jogador:
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
    

#chamados de metodos de classes
game = Jogo()

pontos = Pontuacao()

menu = Menu()

player = Jogador()

mob = Personagem()

bixo = Inimigo()

"""
while True:
    acao = int(input(f"Menu: digite o valor da ação\n1: Iniciar Jogo\n2: Mostrar Opções\n3: Sair\n"))
    if acao == 2:
        print("Escolha a opção com base no valor")
        menu.mostrar_opcoes()
        dificul = int(input())
        match dificul:
            case 1:
                bixo.definir_vida(50)
            case 2:
                bixo.definir_vida(100)
            case 3:
                bixo.definir_vida(200)
    elif acao == 1:
        menu.iniciar_jogo(game)
        inimigos = random.randint(1,3)
        derrotados = 0
        while mob.vida > 0 and bixo.vida > 0 and derrotados != inimigos:
            acao = int(input(f"Você tem {mob.vida} pontos de vida e {player.energia} pontos de energia\nO que vai fazer: digite o valor da ação\n1: Atacar\n2: Descansar\n"))
            if acao == 1 and player.energia > 0:
                dano = random.randint(5,20)
                player.atacar(bixo, dano)
                if bixo.vida <= 0:
                    print(f"O {bixo.nome} foi derrotado")
                    pontos.adicionar_pontos(10)
                    bixo.vida=100
                    derrotados+=1
                dano = random.randint(5,20)
                bixo.atacar(mob, dano)
                if mob.vida <= 0:
                    print(f"O {mob.nome} foi derrotado")
                    mob.fim_de_jogo()
                    break
            elif acao == 1 and player.energia <= 0:
                print(f"O {mob.nome} esta sem energia para atacar")
            
            elif acao == 2:
                player.recuperar_energia(20)
    elif acao == 3:
        menu.sair()
        break
    else:
        print("Ação invalida")
"""