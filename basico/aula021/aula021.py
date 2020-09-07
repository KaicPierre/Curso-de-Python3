"""
For/Else em Python
O laço for também suporta um laço else.
"""

lista = ['Kaic', 'Pierre', 'Python']

for contador in lista:

    if contador.startswith('P'):
        print(f'{contador} começa com P')

    else:
        print(f'{contador} não começa com P')
