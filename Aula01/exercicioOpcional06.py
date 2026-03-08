#Imprima os valores de `1` a `100` usando um laço `for`. Para os números múltiplos de 3,
#imprima “Fizz” ao invés do número, para os múltiplos de 5 imprima “Buzz” e para os
#múltiplos de 3 e 5, imprima “FizzBuzz”.

for i in range(1, 101):
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)