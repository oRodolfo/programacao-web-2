from ReservaVoo import ReservaVoo

if __name__ == "__main__":
    reserva1 = ReservaVoo()

    semassentoespecial = reserva1.calcular_passagem(800.00)
    print(f"TOTAL (SEM ASSENTO ESPECIAL): R$ {semassentoespecial:.2f}")

    comassentoespecial = reserva1.calcular_passagem(1200.00, 150.00)
    print(f"TOTAL (COM ASSENTO ESPECIAL): R$ {comassentoespecial:.2f}")