import random

def validar_resposta_usuario(opcoes):
    while True:
        try:
            resposta_usuario = int(input(f'Escolha uma opção, de 1 a {len(opcoes)}: '))
            if 1 <= resposta_usuario <= len(opcoes):
                return resposta_usuario
            else:
                print(f'Opção inválida, escolha um número de 1 a {len(opcoes)}')
        except ValueError:
            print('Digite um número')

def verificar_resposta(pergunta, resposta_usuario):
    opcoes = pergunta['Opções']
    resposta_correta = pergunta['Resposta']
    
    valor_indice = opcoes.index(resposta_correta) + 1

    if valor_indice == resposta_usuario:
        print('Parabéns, você é muito inteligente!')
        return True
    else:
        print(f'Que droga, você errou! A resposta correta é a opção {valor_indice}: {resposta_correta}')
        return False

def fazer_perguntas(perguntas):
    random.shuffle(perguntas)
    pontuacao = 0

    for i, pergunta_info in enumerate(perguntas, start=1):
        pergunta = pergunta_info['Pergunta']
        opcoes = pergunta_info['Opções']

        print(f"\n{i}. {pergunta}")

        for indice, valor in enumerate(opcoes, start=1):
            print(f'{indice}) {valor}')

        tentativas = 2
        while tentativas > 0:
            resposta_usuario = validar_resposta_usuario(opcoes)
            if verificar_resposta(pergunta_info, resposta_usuario):
                pontuacao += 1
                break
            else:
                tentativas -= 1
                print(f'Você tem mais {tentativas} {"tentativa" if tentativas == 1 else "tentativas"}.')

    print(f'\nQuestionário encerrado! Sua pontuação final é: {pontuacao}/{len(perguntas)}')
    return 'Obrigado por responder!'

perguntas = [
    {
        'Pergunta': 'Maior ou menor país do mundo?',
        'Opções': ['Vaticano e Rússia', 'Nauru e China', 'Mônaco e Canadá', 'São Marino e Índia'],
        'Resposta': 'Vaticano e Rússia',
    },
    {
        'Pergunta': 'Número de elementos químicos na tabela periódica?',
        'Opções': ['95', '119', '118', '113'],
        'Resposta': '118',
    },
    {
        'Pergunta': 'Tempo para a luz do Sol chegar à Terra?',
        'Opções': ['12 minutos', '1 dia', '12 segundos', '8 minutos'],
        'Resposta': '8 minutos',
    }
]

print(fazer_perguntas(perguntas))