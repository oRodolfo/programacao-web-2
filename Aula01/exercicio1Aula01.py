#1


valorA = int(input("Digite um valor: "))
valorB = int(input("Digite um valor: "))
print("""
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Divisao Real
5 - Divisao Inteira
6 - REsto Divisao
7 - Potencia 
""")
operacao = int(input("Informe a operacao q desejada: "))

match operacao:
    case 1:
        print(valorA + valorB)
    case 2:
        print(valorA - valorB)
    case 3:
        print(valorA * valorB)
    case 4:
        print(valorA / valorB)
    case 5:
        print(valorA // valorB)
    case 6:
        print(valorA % valorB)
    case 7:
        print(valorA ** valorB)