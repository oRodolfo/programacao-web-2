#Peça três números ao usuário e informe qual é o maior deles.

numero1 = int(input("Informe um numero: "))
numero2 = int(input("Informe um numero: "))
numero3 = int(input("Informe um numero: "))

if numero1 >= numero2 and numero1 >= numero3:
    print(f"O maior numero é {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"O maior numero é {numero2}")
else:
    print(f"O maior numero é {numero3}")