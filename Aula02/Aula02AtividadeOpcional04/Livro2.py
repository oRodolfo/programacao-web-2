from MaterialBiblioteca2 import MaterialBiblioteca2

class Livro(MaterialBiblioteca2):
    def __init__(self, titulo, ano_publicacao, autor):
        super().__init__(titulo, ano_publicacao)
        self.autor = autor

    def exibir_detalhes(self):
        super().exibirInformacoes()
        print(f"Autor: {self.autor}")