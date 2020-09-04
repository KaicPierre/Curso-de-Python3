nome = 'Kaic Pierre'
idade = 18
altura = 1.80
eh_maior = idade >= 18
peso = 70
imc = peso / (altura ** 2)
print(nome, 'tem', idade, 'anos de idade e seu IMC é de:', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é de: {imc:.2f}')
print('{0} tem {1} anos de idade e seu IMC é de {2}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é de {im}'.format(n = nome, i = idade, im = imc))
