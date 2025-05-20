class Computador():
    def ligar(self):
        print("Ligou!")

class Impressora():
    def imprimir(self):
        print("Print!")
    
class Multifuncao(Computador, Impressora):
    pass

doideira = Multifuncao()

doideira.ligar()
doideira.imprimir()
