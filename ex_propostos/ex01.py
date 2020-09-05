numero_int = input('Informe um número inteiro: ')

try:
    numero_int = int(numero_int)

    if numero_int % 2 == 0:
        print('Número par.')
    else:
        print('Número ímpar.')
except:
    print('O que foi digitado não é um número inteiro.')
