print("Hello World!")
print("Me livrei da maldição!")

contador = 0
while contador < 10:
    nome = input("Qual o seu nome?")
    print(f"Olá {nome}!")

    idade = int(input("Qual a sua idade?"))
    print(idade)

    if(idade <= 18):
        print(f"{nome}  é uma criança")
    elif(idade <= 60):
        print(f"{nome} é um adulto")
    else:
        print(f"{nome} é um idoso")

    contador += 1

