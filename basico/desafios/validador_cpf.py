# Validador de CPF
cpf = ''
soma1 = 0
soma2 = 0
invalidos = ['00000000000', '11111111111', '22222222222',
             '33333333333', '44444444444', '55555555555',
             '66666666666', '77777777777', '88888888888',
             '99999999999']

while not len(cpf) == 11:
    cpf = input('Informe um CPF(sem "." ou "-"): ')

    if cpf.isdigit():
        continue
    else:
        cpf = ''


for indice1, contador1 in enumerate(range(10, 1, -1)):
    soma1 = int(cpf[indice1]) * contador1 + soma1

    if 11 - (soma1 % 11) > 9:
        digito1 = '0'

    else:
        digito1 = str(11 - (soma1 % 11))


for indice2, contador2 in enumerate(range(11, 1, -1)):
    soma2 = int(cpf[indice2]) * contador2 + soma2

    if 11 - (soma2 % 11) > 9:
        digito2 = '0'

    else:
        digito2 = str(11 - soma2 % 11)

if cpf in invalidos:
    print('CPF inválido')

elif digito1 == cpf[-2] and digito2 == cpf[-1]:
    print('CPF válido.')

else:
    print('CPF inválido.')
