"""
Funções def em Python - Parte 3
*args **kwargs
a partir que você colocar um valor padrão em um argumento/parâmetro de uma função
todos os argumntos/parametros depois dele precisam de um valor padrão, o mesmo vale
pra quando se chamar a função.
"""

def function (*args, **kwargs):
    print(args)
    nome = kwargs.get('nome')
    print(nome)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
function(*lista, *lista2, nome='Kaic', sobrenome= 'Pierre')