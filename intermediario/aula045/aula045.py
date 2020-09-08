"""
Funções - def em Python (Parte 1)
Servem para coisas que são repetidas muitas vezes
Recebem Parâmetros nos parenteses
"""

def saudacao(msg='Olá', nome='Usuário'):
    return f'{msg}, {nome}'

# saudacao('Olá', 'Kaic Pierre')
# saudacao(nome='Kaiak')
variavel = saudacao()
print(variavel)
