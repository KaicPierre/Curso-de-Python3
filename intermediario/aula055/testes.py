clientes = {
    'cliente1': {
        'nome': 'Kaic',
        'sobrenome': 'Pierre',
    },
    'cliente2': {
        'nome': 'Rita',
        'sobrenome': 'Pierre',
    },
}

for keys_clientes, value_clientes in clientes.items():

    print(f'Exibindo {keys_clientes}')

    for keys_dados, value_dados in value_clientes.items():

        print(f'\t {keys_dados} = {value_dados}')
