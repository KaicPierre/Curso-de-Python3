nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade?'))

if 20 <= idade <= 30:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} NÃO pode pegar o empréstimo')