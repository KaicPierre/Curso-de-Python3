# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
# set (conjuntos) suporta apenas elementos imutáveis
# não possue indice

set1 = {1, 2, 3, 4, 5}
print(set1)

set2 = set()
set2.add(1)
set2.add(2)

print(set2)

set2.discard(1)
set1.discard(3)

set1.update('Python')

print(set1)

set3 = set1 & set2

print(set3)

lista = [1,1,1,1,1,1,2,4,6,7,'Kaic','Kaic']
lista = set(lista)

print(lista)

lista = list(lista)
print(lista)