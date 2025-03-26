class Camiseta:
    def __init__(self):
        self.nome = None
        self.preco = None
        self.tamanho = None
        self.cor = None
        self.codigo_de_barras = None
        self.quantidade = None

camisa1 = Camiseta()
camisa1.nome = "Melhor camisa do ano"
camisa1.preco = 21.50
camisa1.tamanho = "XG"
camisa1.cor = "Preta"
camisa1.codigo_de_barras = "110011011010001110"
camisa1.quantidade = 10

print(f"A Camisa '{camisa1.nome}' {camisa1.cor} do tamanho {camisa1.tamanho} fica pelo valor em R${camisa1.preco}. {camisa1.quantidade} em estoque\ncodigo do produto: {camisa1.codigo_de_barras}")

class Livro:
    def __init__(self):
        self.nome = None
        self.volume = None
        self.tipo_da_capa = None
        self.preco = None
        self.quantidade = None
livro1 = Livro()
livro1.nome = "Espadachim de Carvão"
livro1.volume = 2
livro1.tipo_da_capa = "Dura"
livro1.preco = 41.10
livro1.quantidade = 4
print(f"\nO Livro {livro1.nome} Volume {livro1.volume} de Capa {livro1.tipo_da_capa} custa R${livro1.preco}\n{livro1.quantidade} em estoque")

class ContaBancaria:
    def __init__(self):
        self.banco = None
        self.agencia = None
        self.tipo = None
        self.senha = None
        self.usuario = None
        self.debito = None

conta = ContaBancaria()
conta.banco = "Banco do Brasil"
conta.agencia = "53801-4"
conta.tipo = "Corrente"
conta.senha = "439104"
conta.usuario = "Joaquim Morais"
conta.debito = 124978

print(f"\nSenhor {conta.usuario}. Sua conta {conta.tipo} no {conta.banco} Agencia {conta.agencia} com R${conta.debito} de debido foi hackeadada. Insira a senha: {conta.senha}\nVocê foi Hackeado")

class Tarefa:
    def __init__(self):
        self.nome = None
        self.cituacao = None
        self.cronograma = None
        self.responsavel = None
        self.local = None

dever = Tarefa()
dever.nome = "Limpar"
dever.cituacao = "Em andamente"
dever.cronograma = "toda tarde de Segunda a Sexta"
dever.responsavel = "Pedro"
dever.local = "Quartos"
print(f"\nA Tarefa de {dever.nome} {dever.local} {dever.cronograma} esta {dever.cituacao} pelo funcionario {dever.responsavel}")

class Termostato:
    def __init__(self):
        self.medidor = None
        self.fabricante = None
        self.modelo = None
        self.local = None
        self.escala = None

termometro = Termostato()
termometro.medidor = "Digital"
termometro.fabricante = "WIKA"
termometro.modelo = "Industrial"
termometro.local = "Subsolo"
termometro.escala = "Grais Celsius"
print(f"\nO Termostato esta medindo 28° {termometro.escala} ")

class DNA:
    def __init__(self):
        self.codigo_genetico = None
        self.quantidade_de_genes = None
        self.tamanho = None
        self.portador = None

class Pixel:
    def __init__(self):
        self.cor = None
        self.valor = None
        self.posição = None
        self.tipo = None

