"""
Expressões Lambda (Funções anônimas)
"""

# var = lambda x, y: x * y
#
# print(var(2, 2))

lista = [
    ['P1', 300],
    ['P2', 400],
    ['P3', 100],
    ['P4', 40],
    ['P5', 210],
]

# def func (item):
#     return item[1]
# Pode ser substituida por uma expressão lambda

# lista.sort(key=lambda item: item[1], reverse=True)  #Pode ser substituido pela função sorted no proprio print, não alterando a variavel lista de fato

print(sorted(lista, key=lambda item: item[1], reverse=True))
print(lista)
