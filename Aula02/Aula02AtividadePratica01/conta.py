class Conta:
    def __init__(self, titulo):
        self.titulo = titulo
        self.saldo = 0.0

    def depositar(self, valor):
        if (valor > 0):
            self.saldo += valor
            print(f"Deposito: R${valor:.2f}")
        else:
            print("Valor indisponivel")

    def sacar(self, valor):
        if (valor > self.saldo):
            print("Valor indisponivel")
        else:
            print(f"VALOR TOTAL: R${self.saldo:.2f}")
            self.saldo -= valor
            print(f"Valor sacado: R${valor:.2f}")
            print(f"SALDO ATUALIZADO: R${self.saldo:.2f}")