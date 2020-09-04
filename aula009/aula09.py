# Entrada de dados
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

ano_nascimento = 2020 - int(idade)

print()

print(f'O usuário digitou {nome} e o tipo da variável é {type(nome)}')
print(f'{nome} tem {idade} anos de idade.')
print(f'{nome} nasceu em {ano_nascimento}')
