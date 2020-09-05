# Iterando strings com while - Passar por cada caracter da string

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
nova_string = ''
contador = 0

# Iteração

while contador <= tamanho_frase:
    print(nova_string, contador + 1, sep=' - ')
    if frase[contador] == 'r':
        nova_string += 'R'
        contador += 1
        continue
    nova_string += frase[contador]
    contador += 1
