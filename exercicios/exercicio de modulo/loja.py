class Loja():
    total_lojas = 0
    def __init__(self, localizacao):
        self.localizacao = localizacao
        Loja.total_lojas+=1
    
    @classmethod
    def quantidade_lojas(cls):
        print(f"Tem {cls.total_lojas} de Lojas")


loja1 = Loja("Picui")
loja2 = Loja("Carnauba dos Dantas")
loja3 = Loja("Joao Pessoa")

Loja.quantidade_lojas()