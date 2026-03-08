class MaterialBiblioteca2:
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    def exibirInformacoes(self):
        print(f"TITULO LIVRO: {self.titulo} | ANO DE PUBLICACAO: {self.ano_publicacao}")