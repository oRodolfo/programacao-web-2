ListaNumeros = []
while True:
    numero = float(input("Digite um número (ou 0 para sair): "))

    if numero == 0:
        break

    ListaNumeros.append(numero)


def numerosPares(ListaNumeros):
    return [n for n in ListaNumeros if n % 2 == 0]


if len(ListaNumeros) > 0:
    pares = numerosPares(ListaNumeros)
    print(f"Lista original: {ListaNumeros}")
    print(f"Números pares: {pares}")
else:
    print("Nenhum número foi digitado.")