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
print(camisa1.nome)