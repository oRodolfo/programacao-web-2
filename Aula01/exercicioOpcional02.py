#Peça a idade de uma pessoa e diga se ela é:
#- Criança (0–12)
#- Adolescente (13–17)
#- Adulto (18–59)
#- Idoso (60+)

idade = int(input("Qual a sua idade? "))

if idade <= 12:
    print("Você é uma criança")
elif idade <= 17:
    print("Você é um adolescente")
elif idade <= 59:
    print("Você é um adulto")
else:
    print("Você é um idoso")