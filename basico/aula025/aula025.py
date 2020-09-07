nome = input('Qual seu nome? ')

if nome:
    print(nome)
else:
    print('Você nçao digitou nada.')

# ^ é exatamente igual a:

print(nome or 'Você não digitou nada.')
