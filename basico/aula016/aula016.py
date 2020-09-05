# Laço de repetição while

"""numero = 0
while numero < 100:
    if numero % 2 == 0:
        numero = numero + 1
        continue
    print(numero)
    numero = numero + 1
print('Acabou')"""

"""coluna = 0

while coluna < 10:
    linha = 0
    while linha < 5:
        print(f'Tem {coluna} colunas e {linha} linhas')
        linha += 1

    
    coluna += 1  # coluna = coluna + 1
print('Acabou')"""

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número:')
    operador = input('Digite um operador: ')

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except:
        print('Você precisa digitar um número!')
        continue

    if operador == '+':
        print(f'= {num_1 + num_2}')
    elif operador == '-':
        print(f'= {num_1 - num_2}')
    elif operador == '*':
        print(f'= {num_1 * num_2}')
    elif operador == '/':
        print(f'={num_1 / num_2}')
    else:
        print('Operador inválido')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break
