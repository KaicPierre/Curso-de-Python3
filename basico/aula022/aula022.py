"""
Split, Join e Enumerate em Python
- Split: Dividir uma # str
- Join: Juntas uma lista # str
- Enumerate: Enumerar elementos da lista # iteráveis
- Pode-se colocar uma lista dentro de outa lista.
"""

string_teste = 'O Kaic Pierre é um programador em formação, Kaic estuda CCO.'
lista_1 = string_teste.split(' ')
lista_2 = string_teste.split(',')
string_nova = ','.join(lista_2)
print(string_nova)

palavra = ''
contagem = 0

for controle in lista_1:
    print(f'A palavra {controle} apareceu {lista_1.count(controle)} vezes na frase.')
    quantidade = lista_1.count(controle)

    if quantidade > contagem:
        contagem = quantidade
        palavra = controle
print('A palavra que apareceu mais vezes é {}'.format(palavra))

"""
for indice, valor in enumerate (lista_2):
    print(indice, valor)
"""


