
# # Exercício - sistema de perguntas e respostas
def conferir(indice, *args):
    resposta = args
    valor_indice = int(resposta[0][indice])
    return valor_indice

def perguntar():
    for i in perguntas:
        pergunta = i['Pergunta']
        print(f'Pergunta {pergunta}')
        opcao = i['Opções']
        for indice, valor in enumerate(opcao):
            print(f'{indice+1}) {valor}')
        while True:
            try:
                resposta_usuario = int(input('Escolha uma opção:  '))
                if 1 <= resposta_usuario <= len(opcao):
                    break
                else:
                    print(f'Opção inválida, escolha um numero de 1 à {len(opcao)}') 
                    continue   
            except ValueError:
                print('Digite umnúmero')
        valor_indice = conferir(resposta_usuario-1, opcao) 
        resposta_correta = int(i['Resposta'])  
        acertos = []
        erros = []
        if valor_indice == resposta_correta:
            print('✅ Você Acertou  ! \n')
            acertos.append('1')
        else:
            print('❌ Você Errou ! \n')
            erros.append('1')
    return f'\n\tResultado: \n\t✅ Acerto(s): [{len(acertos)+1}]\n\t❌ Erro(s): [{len(erros)+1}] '

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
    }]

print(perguntar())