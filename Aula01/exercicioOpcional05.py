#Peça ao usuário um número e mostre a tabuada desse número de `1` a `10`.

numeroTabuada = int(input("Informe um valor para o calculo da tabuada: "))

for i in range(0, 11, 1):
    calculo = numeroTabuada * i
    print(f"{numeroTabuada} x {i} = {calculo}")