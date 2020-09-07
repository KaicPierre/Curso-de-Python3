palavra = 'video'
digitadas = []
tentativas = 3
tamanho = (len(palavra) + 1) * '_'

print(f'Tamanho da Palavra: {tamanho}')
while True:
    print(f'Tentativas Restantes: {tentativas}')
    if tentativas == 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ').lower()

    if len(letra) > 1:
        print('Apenas uma letra por vez')
        continue

    if letra in palavra:
        print(f'A letra {letra.upper()} existe na palavra secreta.')
        digitadas.append(letra)

    else:
        print(f'A letra {letra} NÃO existe na palavra secreta.')
        tentativas -= 1

    vizualizacao = ''

    for letras_descobertas in palavra:

        if letras_descobertas in digitadas:
            vizualizacao += letras_descobertas

        else:
            vizualizacao += '_'

    if vizualizacao == palavra:
        print('Parabens você descobriu a palavra.')
        print(vizualizacao.upper())
        break

    print(vizualizacao.upper())
    print()