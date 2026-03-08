#Crie um programa que sorteie um número de `1` a `100` e peça para o usuário adivinhar.
#O programa deve dar dicas:
#- Se o número digitado é **maior** ou **menor** que o sorteado.
#- O jogo continua até o usuário acertar.

import random

numeroSorteio = random.randint(1, 100)
resposta = -1
tentativas = 0
while(resposta != numeroSorteio):
    resposta = int(input("Informe um numero entre 1 e 100: "))
    if(resposta > numeroSorteio):
        print("Informe um numero menor")
    else:
        print("Informe um numero maior")
    tentativas += 1

    if(resposta == numeroSorteio):
        print(f"O numero secreto era: {numeroSorteio}")
        print("Você acertou o numero do secreto!")
        print(f"Você tentou {tentativas} vezes")
        break