# len não funciona com int, float ou bool

usuario = input('Digite seu usuário: ')

quantidade_caracteres = len(usuario)

if quantidade_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')
