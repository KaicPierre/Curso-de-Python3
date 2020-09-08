"""
Funções - def em python - return - Parte 2
códigos abaixo do return não são mais executados
"""

# def funcao1 (var1):
#     print(var1)
#
# def funcao2 (var2):
#     return var2
#
# variavel1 = funcao1('Valor Desejado')
# variavel2 = funcao2('Valor Desejado')
#
# if variavel1:
#     print(variavel1)
# else:
#     print('Nenhum Valor - variavel1')
#
# if variavel2:
#     print(variavel2)
# else:
#     print('Nenhum Valor - variavel2')

def divisao (n1, n2):
    if n2 != 0:
        return n1 / n2
    return


operacao = divisao(8, 1)
if operacao:
    print(operacao)
else:
    print('Conta inválida')