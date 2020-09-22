lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {f'chave {chave}': valor**2 for chave, valor in enumerate(range(5))}
print(d1, type(d1))

set1 = {valor for valor in range(5)}
print(set1, type(set1))