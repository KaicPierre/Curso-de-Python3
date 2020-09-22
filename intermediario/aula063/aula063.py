# Geradores, Iteradores e Iteráveis em Python
# For converte em tempo de execução uma string(por exemplo) em um iterador, utilizando o next()


import sys
import time

def gera():
    for numero in range(100):
        yield numero
        time.sleep(0.1)

g = gera()

print(g)
for valor in g:
    print(valor)

gerador = (valor for valor in range(100)) # Gerador criado sem função
print(type(gerador))


