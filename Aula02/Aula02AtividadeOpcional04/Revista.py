from MaterialBiblioteca2 import MaterialBiblioteca2

class Revista(MaterialBiblioteca2):
    def __init__(self, titulo, ano_publicacao, edicao):
        super().__init__(titulo, ano_publicacao)
        self.edicao = edicao

    def exibir_edicao(self):
        super().exibirInformacoes()
        print(f"Edicao {self.edicao}")
