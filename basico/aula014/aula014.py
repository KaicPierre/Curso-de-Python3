# Formatação de valores com modificadores
# :s - Strings
# :d - Inteiros
# :f - Float
# :.(NÚMERO)f - quantidade de casas decimais (float)
# :(CARACTERE)(> ou < ou ^)(QUANTIDADE) (TIPO - s, d, ou f)
# > - Esquerda // < - Direita // ^ - Centro


num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10.2f}')




# divisão = num_1 / num_2

# print('{:.2f}'.format(divisão))
# print(f'{divisão:.2f}')

nome = 'Kaic'
sobrenome = 'Pierre'
print(f'{nome:#^10}')

nome_formatado = '{1} {0}'.format(nome, sobrenome)
print(nome_formatado)

print(nome.ljust(20, '#'))
print(nome.lower())
print(nome.upper())
print(nome.title())