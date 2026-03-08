#Peça um número inteiro `n` e mostre todos os números de `1` até `n`.

valorN = int(input("Digite um numero inteiro: "))

print(f"Fazendo a contagem de 1 até {valorN}: ")
for c in range(1, valorN + 1):
    print(c)