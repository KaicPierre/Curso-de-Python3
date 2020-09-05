nome = 'Kaic Pierre Silva'
idade = 18
altura = 1.80
peso = 71.3
ano_atual = 2020
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
