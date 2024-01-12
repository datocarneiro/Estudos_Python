perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
def apresentar_pergunta(pergunta):
    print(pergunta['Pergunta'])
    while True:
        opcoes = input(f"Escolha uma das alternativas: {', '.join(pergunta['Opções'])} ")
        resposta = pergunta['Resposta']
        if opcoes == resposta:
            return 'Você ACERTOU ... :)'
        else:
            print(f'Sua resposta foi "{opcoes}"... Você ERROU ....:(')
            continue
while True:
    try:
        escolher_questao = int(input('Escolha uma pergunta: 1, 2 ou 3? ')) - 1
        print(escolher_questao)
        if 0 <= escolher_questao < len(perguntas):
            print(apresentar_pergunta(perguntas[escolher_questao]))
        else:
            print('Número inválido')
    except ValueError:
        print('Digite um número')
