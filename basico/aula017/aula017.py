"""
contador = 1
while contador <= 100:
    print(contador)
    contador += 1
"""

# O laço While em python pode ter um Else também, serve pra caso em tenha um
# break ou um continue dentro do while que não torne nescessariamente a verificação dele
# falsa
contador = 1
acumulador = 1
while contador <= 100:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no Else')