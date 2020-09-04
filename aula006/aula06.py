"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Kaic Pierre'
idade = 18
altura = 1.80
eh_maior = idade >= 18
peso = 70
imc = peso / (altura ** 2)

print('Nome', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', eh_maior)
print(nome, 'tem', idade, 'anos de idade e seu IMC é de:', imc)
