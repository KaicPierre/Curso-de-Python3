"""
Desempacotamento de listas em Python
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v1, v2, v3, v4, v5, *lista_2, ultimo = lista
# v1, v2, v3 ... são variaveis baseadas nos índices da lista
# "*" faz a contagem ser ao contrario e previne o erro de ter itens demais para desempacotar


print(v1, v4)
print(lista_2)

