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
        print(f"{self.nome} ataca causando {self.__forca} de dano.")

    

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
    
    def falar(self):#função adicionada nesse capitulo
        print("Eu corro nas sombras da destruição para que ninguém precise abandonar a luz.")
    

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


#classes criadas nesse capitulo

class Arma(): 
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

class Missao(): 
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def descrever_missao(self):
        print(self.descricao)
    
class Item():
    def __init__(self, nome):
        self.nome = nome

class Fase:
    def __init__(self, nome):
        self.nome = nome

class Aliado:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.defesa = 50

#classe hedeiras

class NPC(Jogador):
    def __init__(self, vida, nome, defesa):
        super().__init__(vida, nome, defesa)
    
    def atacar(self):
        print(f"O NPC não pode atacar")

    def falar(self):
        print("Saudações, viajante.")


class Chefe(Inimigo):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida * 2, forca * 2)

    def atacar(self):
        dano = self.__forca + (self.__forca * 0.5)
        print(f"{self.nome} usa um golpe especial causando {dano} de dano total!")


class JogadorPremium(Pontuacao):
    def __init__(self):
        super().__init__()

    @pontos.setter
    def pontos(self,valor):
        if valor >= 0:
            self.__pontos+=valor*2
            print(self.pontos())
        else:
            print("Valor invalido")


class JogoMultiplayer(Jogo):
    def __init__(self):
        super().__init__()
        self.jogadores= []

    def adicionar_jogadores(self, jogador):#Função que adiciona o jogadores no jogo
        self.jogadores.append(jogador)


class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)
        self.configuracoes = {} 

    def personalisar(self, chave, valor):
        self.configuracoes[chave] = valor
        print(f"Configuração '{chave}' salva como: {valor}")


class Arco(Arma):
    def __init__(self, dano, nome="Arco"):
        super().__init__(nome, dano)

    def ataque(self):
        print(f"O Disparo com o {self.nome} causou {self.dano} ao alvo")


class Espada(Arma):
    def __init__(self, dano, nome="Espada"):
        super().__init__(nome, dano)

    def ataque(self):
        print(f"O Golpe com a {self.nome} causou {self.dano} ao alvo")


class MissaoPrincipal(Missao):
    def __init__(self, nome, descricao):
        super().__init__(nome, descricao)

    def concluir_missao(self):
        print(f"A Missão {self.nome} foi concluida\nSua recompensa: $1000 + 1000xp")


class MissaoSecundaria(Missao):
    def __init__(self, nome, descricao):
        super().__init__(nome, descricao)

    def concluir_missao(self):
        print(f"A Missão {self.nome} foi concluida\nSua recompensa: $400 + 100xp")

class Pocao(Item):
    def __init__(self, nome, efeito):
        super().__init__(nome)
        self.efeito = efeito
    
    def usar_pocao(self):
        print(f"A {self.nome} foi usanda e lhe deu {self.efeito}")

class Equipamento(Item):
    def __init__(self, nome, tipo, bonus):
        super().__init__(nome)
        self.tipo = tipo
        self.bonus = bonus
        self.equipado = False

    def equipar(self):
        if not self.equipado:
            print(f"Você equipa seu {self.nome} no espaço de {self.tipo} e ganha {self.bonus}")
            self.equipado = True
        else:
            print(f"Ja esta equipado")

    def desequipar(self):
        if self.equipado:
            print(f"Você desequipa seu {self.nome} e perde o bonus de {self.bonus}")
            self.equipado = False
        else:
            print(f"Não esta equipado")


class FaseFloresta(Fase):
    def __init__(self,nome):
        super().__init__(nome)

    def ambientacao(self):
        print(f"A densa floresta de {self.nome} se ergue à sua frente. Sons de folhas e animais ecoam por todo lado, mantendo você em alerta constante.")
    

class FaseDeserto(Fase):
    def __init__(self,nome):
        super().__init__(nome)

    def ambientacao(self):
        print(f"O calor escaldante do deserto {self.nome} torna cada passo mais pesado. O suor escorre, testando sua determinação a cada instante.")


class Guerreiro(Aliado):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.defesa=100
    
    def usar_habilidade(self):
        print(f"O golpe poderoso de {self.nome} faz o chão tremer, abrindo fissuras e derrubando tudo ao redor.")


class Mago(Aliado):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.defesa=25

    def usar_habilidade(self):
        print(f"{self.nome} traça runas no ar e canaliza uma explosão de energia arcana que consome tudo no caminho.")

