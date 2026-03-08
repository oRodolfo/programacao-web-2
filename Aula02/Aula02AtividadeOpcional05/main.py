from geometria import Retangulo

if __name__ == "__main__":
    meu_retangulo = Retangulo(base=10, altura=20)
    area = meu_retangulo.calcular_area()
    print(f"Base: {meu_retangulo.base}")
    print(f"Altura: {meu_retangulo.altura}")
    print(f"A área do retângulo é: {area}")