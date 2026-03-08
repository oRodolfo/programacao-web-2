from conta import Conta


class Conta_Corrente(Conta):

    def __init__(self, titulo, limite):
        super().__init__(titulo)
        self.limite = limite

    def sacar(self, valor):
        total_disponivel = self.saldo + self.limite

        if valor > total_disponivel:
            print("Limite insuficiente!")
            return False

        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado.")
        print(f"Saldo atual: R${self.saldo:.2f}")
        return True