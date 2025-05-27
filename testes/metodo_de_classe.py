class Banco():
    total_contas = 0
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        Banco.total_contas += 1

    @classmethod
    def exibir_total_contas(cls):
        print(f"Total de contas criadas: {cls.total_contas}")

jorge = Banco("Jorge", 200)

Banco.exibir_total_contas()

maria = Banco("Maria", 2000)

Banco.exibir_total_contas()