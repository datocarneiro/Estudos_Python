perguntas = [{
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },{
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },{
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
def escolher_pergunta(indice):
    print(indice)
    dados_pergunta_escolhida = perguntas[indice] # dicionario
    print(dados_pergunta_escolhida.get('Pergunta'))
    while True:
        opcoes = input(f"Escolha uma das alternativas: {dados_pergunta_escolhida.get('Opções')}")
        resposta = dados_pergunta_escolhida.get('Resposta')
        if opcoes == resposta:
            return 'Você ACERTOU ... :)'
        else:
            print(f'Sua resposta foi "{opcoes}"... Você ERROU ....:(')
            continue

while True:
    try:
        escolher_questao = int(input(f'escolha uma pergunta: 1, 2 ou 3?'))-1
        if escolher_questao < 0 or escolher_questao > 2:
            print('Numero inválido')
            continue
        else:
            for i,v  in enumerate(perguntas):
                    if escolher_questao == i:
                        print(escolher_pergunta(escolher_questao))
    except ValueError:
        print('Digite um número')
