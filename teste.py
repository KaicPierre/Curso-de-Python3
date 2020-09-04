nome = input('Olá, qual o seu nome? ')
idade = int(input(f'{nome}, quantos anos você têm? '))
if idade >= 18:
    print(f'Muito prazer em conhecer você {nome}! Acesso concedido.')
else:
    print(f'Muito prazer em conhecer você {nome}, infelizmente o acesso é permitido apenas para maiores de 18 anos! Acesso negado.')
