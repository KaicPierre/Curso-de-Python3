"""
Operadores Lógicos
and, or, not
in e not in
"""

# not inverte o valor da expressão
# in serve para checar se está presente em algo
"""
EXEMPLO:
 nome = Kaic
 if 'K' in nome:
    print(existe)   
"""

usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Kaic'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha invalidos.')
