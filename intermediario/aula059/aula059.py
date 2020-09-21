
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [valor for valor in l1]  # Iteração em apenas uma linha

ex2 = [valor * 2 for valor in l1]

ex3 = [(valor1, valor2) for valor1 in l1 for valor2 in range(3)]

l2 = ['Kaic', 'Pierre', 'Silva']
ex4 = [valor.replace('a', '@') for valor in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 = [(y, x) for x, y in tupla]

l3 = list(range(100))
ex6 = [valor for valor in l3 if valor % 3 == 0 if valor % 8 == 0]
ex7 = [valor if valor % 3 == 0 else 0 for valor in l3]

print(ex6)
print(ex7)
print(dict(ex5))
print(ex4)
print(ex3)
