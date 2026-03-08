class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def vender(self, quantidade):
        if(quantidade <= self.quantidade_estoque):
            self.quantidade_estoque -= quantidade
            valor_total = quantidade * self.preco
            print(f"Venda realizada: {quantidade} {self.nome}(s).")
            print(f"Valor total da venda: R$ {valor_total:.2f}")
            print(f"Estoque atual: {self.quantidade_estoque}")
        else:
            print("Quantidade indisponivel no estoque")