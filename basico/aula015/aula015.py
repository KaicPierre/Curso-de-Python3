"""
Manipulando Strings

- String índices
- Fatiamento de Strings [inicio:fim:passo]
- Funções Built-in len, abs, type, print, etc
Essas funções podem ser usadas diretamente em cada tipo.

indicie positivo [123456789]
indice negativo -[987654321]
"""

texto = 'Python <3'
print(texto[8])

# remover o último caractere
url = 'www.google.com.br/'
print(url[:-1])

# possibilidades para fatiar com indices
# [inicio(incluso):fim(não incluso):pulando de tanto em tanto]
nova_string = texto[:6]
print(nova_string)
print(texto[7:])
print(texto[0:6:2])
print(texto[:len(texto) - 1])
