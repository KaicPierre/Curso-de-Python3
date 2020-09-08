variavel = 'Valor'

def function1():
    print(variavel)
    variavel = 'Local'

def function2():
    global variavel  # Não é uma boa prática!
    variavel = 'Outro Valor'
    print(variavel)

function1()