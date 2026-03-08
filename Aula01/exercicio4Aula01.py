#4) Escreva uma função que receba a base e a alturade um triângulo e retorne sua área

def areaTriangulo(base, altura):
    area = (base*altura)/2
    return area

valorA = int(input("Informe um valor: "))
valorB = int(input("Informe um valor: "))
print("Area do triangulo: ", areaTriangulo(valorA, valorB))