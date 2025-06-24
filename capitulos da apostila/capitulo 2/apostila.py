import random

#criação de classes
#continuação do capitulo 2

class Jogo:
    def __init__(self):
        self.__dificuldade = 2
        self.menu = None

    def definir_menu(self, texto = "Menu Principal"):
        self.menu = Menu(texto)

    
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
        print(f"{self.nome} ataca causando {self.__forca} de dano")

    

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
        self.missoes = []

    def aceitar_missao(self, missao):
        self.missoes.append(missao)
        print(f"{self.nome} aceitou a missão: {missao.nome}")


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
        print("Eu corro nas sombras da destruição para que ninguém precise abandonar a luz")
    

class Jogador():
    def __init__(self, nome, energia, pontos):
        self.__energia = energia
        self.nome = nome
        self.pontos = pontos
        self.arma = None
        self.aliado = None

    def adicionar_aliado(self, aliado):
        self.aliado = aliado
        print(f"{aliado.nome} agora esta te acompanhando na aventura")

    def equipar_arma(self, arma):
        self.arma = arma
        print(f"{self.nome} equipou a arma {arma.nome} com {arma.dano} de dano")

    
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
        self.monstros = ["Goblin", "Lobo Selvagem", "Esqueleto Errante", "Morcego Sombrio"]
        self.inimigos = self.conjunto_inimigos()

    def conjunto_inimigos(self):
        return [Inimigo(nome, 100, 10) for nome in self.monstros]

    def gerar_inimigos(self):
        monstro = random.choice(self.monstros)
        print(f"Um {monstro} aparece na fase {self.nome}!")


class Aliado:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.defesa = 50

class Voador:
    def __init__(self):
        pass

    def voar(self):
        print(f"{self.nome} alça voo pelos céus com majestade!")


class Curador:
    def __init__(self):
        pass

    def curar(self, aliado, quantidade):
        aliado.vida += quantidade
        print(f"{self.nome} cura {aliado.nome} em {quantidade} pontos de vida! Agora {aliado.nome} tem {aliado.vida} de vida")


class MagiaElemental:
    def lançar_magia(self, elemento):
        match elemento.lower():
            case "fogo":
                print(f"{self.nome} conjura uma bola de fogo que incinera os inimigos!")
            case "água" | "agua":
                print(f"{self.nome} invoca um jato de água cortante como lâmina!")
            case "terra":
                print(f"{self.nome} ergue pilares de pedra que esmagam tudo ao redor!")
            case "ar":
                print(f"{self.nome} convoca uma rajada de vento que lança os inimigos pelos ares!")
            case _:
                print(f"{self.nome} tentou conjurar um elemento desconhecido... Nada aconteceu")

class AnimalMontaria:
    def montar(self, criatura):
        print(f"{self.nome} monta em seu {criatura}, pronto para a batalha com força e velocidade redobradas!")


class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_ao_inventario(self, nome_do_item):
        self.itens.append(Item(nome_do_item))
        print(f"{nome_do_item} foi adicionado ao inventario")


class Guilda:
    def __init__(self, nome):
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, jogador):
        self.membros.append(jogador)
        print(f"{jogador.nome} entrou na guilda {self.nome}")

class Mapa:
    def __init__(self):
        self.fases = []

    def adicionar_fase(self, fase):
        self.fases.append(fase)
        print(f"Fase {fase.nome} adicionada ao mapa")

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.itens_disponiveis = []

    def adicionar_item(self, item):
        self.itens_disponiveis.append(item)
        print(f"{item.nome} adicionado na loja {self.nome}")


class SistemaCombate:
    def __init__(self, personagem, inimigo):
        self.personagem = personagem
        self.inimigo = inimigo

    def iniciar_combate(self):
        print(f"{self.personagem.nome} enfrenta {self.inimigo.nome} em um duelo mortal!")

    def encerrar_combate(self):
        print("Combate encerrado")
        del self.personagem
        del self.inimigo


#classe hedeiras

class NPC(Jogador):
    def __init__(self, vida, nome, defesa):
        super().__init__(vida, nome, defesa)
    
    def atacar(self):
        print(f"O NPC não pode atacar")

    def falar(self):
        print("Saudações, viajante")


class Chefe(Inimigo):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida * 2, forca * 2)

    def atacar(self):
        dano = self.__forca + (self.__forca * 0.5)
        print(f"{self.nome} usa um golpe especial causando {dano} de dano total!")


class JogadorPremium(Pontuacao):
    def __init__(self, pontos):
        super().__init__(pontos)

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

    def iniciar(self):
        if not self.jogadores:
            print("Não é possível iniciar o jogo multiplayer: nenhum jogador conectado")
        else:
            print(f"O jogo multiplayer vai começou com: {len(self.jogadores)} jogador/es")


class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)
        self.configuracoes = {} 

    def personalisar(self, chave, valor):
        self.configuracoes[chave] = valor
        print(f"Configuração '{chave}' salva como: {valor}")

    def mostrar_opcoes(self):
        super().mostrar_opcoes()
        print("\nOpções Avançadas:\n4: Multiplayer\n5: Sobrevivência")


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
        self.monstros = ["Ent Sombrio","Aranha Venenosa","Fera da Névoa","Espírito da Floresta"]
    
    def ambientacao(self):
        print(f"A densa floresta de {self.nome} se ergue à sua frente. Sons de folhas e animais ecoam por todo lado, mantendo você em alerta constante")
    
    def gerar_inimigos(self):
        monstro = random.choice(self.monstros)  
        print(f"Da escuridão de {self.nome}, surge um(a) {monstro} entre as árvores!")


class FaseDeserto(Fase):
    def __init__(self,nome):
        super().__init__(nome)
        self.monstros_deserto = ["Escorpião Gigante","Múmia","Verme da Areia","Elemental de Areia"]

    def ambientacao(self):
        print(f"O calor escaldante do deserto {self.nome} torna cada passo mais pesado. O suor escorre, testando sua determinação a cada instante")
    
    def gerar_inimigos(self):
        monstro = random.choice(self.monstros)
        print(f"No deserto {self.nome}, surge um {monstro} das dunas!")



class Guerreiro(Aliado):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.defesa=100
    
    def usar_habilidade(self):
        print(f"O golpe poderoso de {self.nome} faz o chão tremer, abrindo fissuras e derrubando tudo ao redor")


class Mago(Aliado):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.defesa=25

    def usar_habilidade(self):
        print(f"{self.nome} traça runas no ar e canaliza uma explosão de energia arcana que consome tudo no caminho")

class Dragao(Inimigo, Voador):
    def __init__(self, nome, vida, forca, elemento):
        super().__init__(nome, vida, forca)
        self.elemento = elemento

class Paladino(Guerreiro, Curador):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def usar_habilidade(self):
        print(f"{self.nome} ergue sua espada sagrada, causando dano e protegendo seus aliados com luz divina!")


class MagoElemental(Mago, MagiaElemental):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)


class Cavaleiro(Guerreiro, AnimalMontaria):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def usar_habilidade(self):
        print(f"{self.nome}, montado em sua criatura, desfere um golpe brutal que arrasa tudo à frente!")