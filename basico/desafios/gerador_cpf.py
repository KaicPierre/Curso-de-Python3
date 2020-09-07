# Gerador de CPF
from random import randint

cpf = str(randint(000000000, 999999999))

soma1 = 0
soma2 = 0
invalidos = ['000000000', '111111111', '222222222',
             '333333333', '444444444', '555555555',
             '666666666', '777777777', '888888888',
             '999999999']

while not len(cpf) == 11 and not cpf in invalidos:
    for indice1, contador1 in enumerate(range(10, 1, -1)):
        soma1 = int(cpf[indice1]) * contador1 + soma1

        if 11 - (soma1 % 11) > 9:
            digito1 = '0'

        else:
            digito1 = str(11 - (soma1 % 11))

    cpf = cpf + digito1


    for indice2, contador2 in enumerate(range(11, 1, -1)):
        soma2 = int(cpf[indice2]) * contador2 + soma2

        if 11 - (soma2 % 11) > 9:
            digito2 = '0'

        else:
            digito2 = str(11 - soma2 % 11)

    cpf = cpf + digito2

print(f'CPF Gerado: {cpf}')
