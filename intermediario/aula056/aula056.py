perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'A': '5',
            'B': '4',
            'C': '2',
            'D': 'Nenhuma das anteriores',
        },
        'respostaCerta': 'B',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5x5?',
        'respostas': {
            'A': '50',
            'B': '10',
            'C': '5555',
            'D': '25',
        },
        'respostaCerta': 'D',
    },

}

print()
respostasCorretas = 0

for chavePergunta, valorPergunta in perguntas.items():
    print(f'{chavePergunta}: {valorPergunta["pergunta"]}')
    print('Escolha uma das alternativas abaixo: ')

    for chaveRespostas, valorResposta in valorPergunta['respostas'].items():
        print(f'[{chaveRespostas}]: {valorResposta} ')

    alternativa = input('Alternativa escolhida: ').capitalize()
    print()

    if alternativa == valorPergunta['respostaCerta']:
        print('Resposta Correta!')
        respostasCorretas += 1
    else:
        print('Resposta incorreta!')
        print(f'Alternativa Correta: [{valorPergunta["respostaCerta"]}]')
    print()

    porcentagemAcerto = respostasCorretas / len(perguntas) * 100
print('=' * 30)
print(f'Você acertou: {respostasCorretas} questão(ões)')
print(f'Porcentagem de Acerto: {porcentagemAcerto}%')
print('=' * 30)
