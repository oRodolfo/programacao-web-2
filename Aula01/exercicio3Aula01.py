#3) Crie uma lista com as notas [7.5, 8.0, 6.0, 9.5,10.0].
#● Adicione uma nova nota à lista;
#● Remova a menor nota;
#● Mostre a média final.

notas = [7.5, 8.0, 6.0, 9.5, 10.0]
print("Lista nota original: ", notas)

notas.append(2.5)
print("Lista com a nova nota adicionada: ", notas)

notas.remove(min(notas))
print("Lista com a menor nota removida: ", notas)

media = sum(notas)/len(notas)
print("Media total: ", media)