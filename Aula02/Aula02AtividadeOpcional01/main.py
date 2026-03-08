from Produto import Produto

if __name__ == "__main__":
    produto1 = Produto("Feijão", 10.90, 10)
    produto1.vender(2)
    print("\n")
    produto2 = Produto("Acer Nitro 5", 2500.00, 5)
    produto2.vender(1)
    print("\n")
    produto3 = Produto("Geladeira", 3500.00, 5)
    produto3.vender(5)