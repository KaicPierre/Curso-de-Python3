"""
Dicionários suportam par de chaves e um valor
Chaves precisam ser únicas nos dicionários, ou seja, seu "índice" precisa ser único
nomes das chaves precisam contem valores imutaveis
"""

d1 = {'chave1': 'Valor da chave',
      'chave2': 'Valor da chave2',
      123: 'Outro Valor',
      (1,2,3,4): 'Tupla'
      }

d1['naoexiste'] = 'Agora existe'
d1.update({'nova_chave': 'Novo Valor'})

if 'naoexiste' in d1:
    print(d1['naoexiste'])

del d1[(1,2,3,4)]
print(d1)
print('chave1' in d1)
print('chave1' in d1.keys())
print('Outro Valor' in d1.values())
print(len(d1))  #Mostra quantos pares tem-se no dicionário

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)

# Outra forma de criar dicionários
# d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
# print(d1)
