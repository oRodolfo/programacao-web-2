from MaterialBiblioteca2 import MaterialBiblioteca2
from Livro2 import Livro
from Revista import Revista

if __name__ == "__main__":
    meu_livro = Livro("O Hobbit", 1937, "J.R.R. Tolkien")
    minha_revista = Revista("National Geographic", 2023, "Edicao Especial")

    meu_livro.exibirInformacoes()
    minha_revista.exibir_edicao()