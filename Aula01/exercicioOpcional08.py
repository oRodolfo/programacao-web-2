#Peça ao usuário para digitar vários números até que ele digite `0`.
#Depois, mostre a média dos números digitados.

somaValores = 0
contandoNumeros = 0
while True:
    numero = float(input("Digite um número (ou 0 para sair): "))

    if numero == 0:
        break

    somaValores += numero
    contandoNumeros += 1

if contandoNumeros > 0:
    media = somaValores / contandoNumeros
    print(f"Você digitou {contandoNumeros} números.")
    print(f"A média é: {media:.2f}")
else:
    print("Nenhum número foi digitado além do 0.")