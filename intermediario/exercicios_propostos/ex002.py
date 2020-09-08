def soma (n1, n2, n3):
    if float(n1) and float(n2) and float(n3):
        soma = n1 + n2 + n3
        print(soma)
    else:
        print('Valor não numérico detectado')

soma(1, 5.5, 15)