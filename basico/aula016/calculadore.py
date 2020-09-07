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
