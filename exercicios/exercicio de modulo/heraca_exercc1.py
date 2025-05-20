class Veiculo():
    def __init__(self, tipo):
        self.tipo = tipo

    def mover(self, metros):
        print(f"{self.tipo} se moveu {metros} metros")


class Bicicleta(Veiculo):
    def __init__(self, tipo, modelo):
        super().__init__(tipo)
        self.modelo = modelo
    
    def pedalar(self, pedaladas):
        print(f"Você deu {pedaladas} pedaladas em sua {self.modelo}")

class Onibus(Veiculo):
    def __init__(self, tipo, capacidade):
        super().__init__(tipo)
        self.quantidade_passageiros = 0
        self.capacidade = capacidade

    def embarcar_passageiros(self, quantidade):
        if self.quantidade_passageiros+quantidade > self.capacidade:
            print("Onibus lotou")
        
        elif self.quantidade_passageiros+quantidade < 0:
            print("Invalido")

        else:
            self.quantidade_passageiros+=quantidade
            print(f"Entraram mais {quantidade} passageiros no onibus")


carro = Veiculo("Carro")
serra_osso = Bicicleta("Bicicleta", "BMX")
binha = Onibus("Onibus", 30)

carro.mover(10)


serra_osso.pedalar(5)
serra_osso.mover(10)


binha.embarcar_passageiros(10)
binha.mover(10)