class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

if __name__ == "__main__":
    print("--- Teste local do módulo geometria.py ---")
    ret_teste = Retangulo(10, 5)
    print(f"Área de teste: {ret_teste.calcular_area()}")