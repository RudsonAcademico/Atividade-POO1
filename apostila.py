import random

#criação de classes

class Jogo:
    def __init__(self):
        pass

    def iniciar(self):
        print("O jogo começou!")
    
    def pular(self):
        print("O personagem pulou!")


class Inimigo:
    def __init__(self):
        self.nome = "Monstrinho"
        self.vida = None

    def definir_vida(self, quantidade):
        self.vida = quantidade


    def atacar(self, alvo, quantidade):
        print(f"O inimigo atacou! e lhe causou {quantidade} de dano")
        alvo.vida-=quantidade

class Pontuacao():
    def __init__(self):
        self.pontos = 0

    def zerar_pontos(self):
        self.pontos = 0
        print("Pontuação zerada!")
    
    def mostrar_pontos(self):
        print(f"Pontuação atual: {self.pontos}")

    def adicionar_pontos(self, quantidade):
        self.pontos+=quantidade
        self.mostrar_pontos()

class Personagem:
    def __init__(self):
        self.vida = 100
        self.nome = input("Digite o nome do seu personagem: ")
    
    def dizer_nome(self):
        print(f"Meu nome é {self.nome}")

    def tomar_dano(self, dano):
        self.vida-=dano
        if self.vida <= 0:
            print("Game Over!") 
            

    def fim_de_jogo(self):
        print("Game Over!")
        
    

class Jogador:
    def __init__(self):
        self.energia = 100
    
    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        if self.energia > 100:
            print("você esta com energia maxima")
            self.energia = 100
        else:
            print(f"Você recuperou {quantidade} pontos de energia")
    
    def usar_energia(self, quantidade):
        self.energia -= quantidade
        if self.energia <= 0:
            print("Sem energia suficiente!")

    def atacar(self, alvo, quantidade):
        print(f"Você atacou! e causou {quantidade} de dano")
        alvo.vida-=quantidade
        self.usar_energia(10)

class Menu:
    def __init__(self):
        pass
    
    def iniciar_jogo(self, game):
        game.iniciar()
    
    def mostrar_opcoes(self):
        print("Modos de Jogo:\nFacil\nMédio\nDificil")
    
    def sair(self):
        print("O Jogo foi Fechado")
    

#chamados de metodos de classes
game = Jogo()

pontos = Pontuacao()

menu = Menu()

player = Jogador()

mob = Personagem()

bixo = Inimigo()

while True:
    
    while mob.vida > 0 and bixo.vida > 0:
        acao = int(input(f"Você tem {mob.vida} pontos de vida e {player.energia} pontos de energia\nO que vai fazer: digite o valor da ação\n1: Atacar\n2: Descansar\n"))
        if acao == 1 and player.energia > 0:
            dano = random.randint(5,20)
            player.atacar(bixo, dano)
            if bixo.vida <= 0:
                print(f"O {bixo.nome} foi derrotado")
                pontos.adicionar_pontos(10)
                bixo.vida=100
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