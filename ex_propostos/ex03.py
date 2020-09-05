primeiro_nome = input('Digite seu primeiro nome: ')

if len(primeiro_nome) <= 4:
    print("Seu nome é curto.")
elif len(primeiro_nome) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
