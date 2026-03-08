from conta_corrente import Conta_Corrente
from conta import Conta

if __name__ == "__main__":
    conta1 = Conta_Corrente("Rodolfo", 1500)
    print(f"Saldo inicial da conta de {conta1.titulo}: SALDO: R${conta1.saldo:.2f} ")

    conta1.depositar(550)
    print(f"Saldo disponivel da conta de {conta1.titulo} R${conta1.saldo:.2f} | LIMITE: R${conta1.limite}")

    conta1.sacar(480)
    print(f"Saldo atualizado após sacar dinheiro: R${conta1.saldo:.2f} | LIMITE: R${conta1.limite}")

    conta1.sacar(1800)
    print(f"Saldo atualizado após sacar dinheiro: R${conta1.saldo:.2f} | LIMITE: R${conta1.limite}")

    print()
    conta2 = Conta("Neymar")
    conta2.depositar(100)
    conta2.sacar(200)

    print()
    conta1.sacar(1570)

    print()
    conta1.depositar(2000)
    print(f"Saldo atualizado {conta1.saldo:.2f}")