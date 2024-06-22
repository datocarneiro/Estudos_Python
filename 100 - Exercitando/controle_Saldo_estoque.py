minimo_alimentos = 50
minimo_bebidas = 75
minimo_limpeza = 30

produtos = {'Feijão': 'Alimentos',
             'Arroz': 'Alimentos',
            'Leite': 'Bebida',
            'Sabão': 'Limpeza'}

lista_produtos = list(produtos)
for i, v in enumerate(lista_produtos):
    print(f'{i+1}) {v}')
while True:
    try:
        item_escolhido = int(input('\nEscolha uma opção: '))-1

        if 0 <= item_escolhido < len(lista_produtos):
            break
        else:
            print('Opção inválida, tente novamente')
    except ValueError:
        print('digite um número')
while True:
    try:
        qtd_estoque = int(input(f'Informar a quantidade em estoque: '))        
        if qtd_estoque >= 0:
            break
        else:
            print('Opção inválida, tente novamente')
    except ValueError:
        print('digite um número')
print()

if  produtos[lista_produtos[item_escolhido]] == 'Alimentos':
    if qtd_estoque < minimo_alimentos:
        print(f'\tSolicitar {lista_produtos[item_escolhido]} á equipe de compras\n\tTemos apenas: {qtd_estoque} und em estoque')
    else:
        print(f'\tEstoque dentro do esperado \n\tTemos: {qtd_estoque} und do item: {lista_produtos[item_escolhido]}')
    
elif produtos[lista_produtos[item_escolhido]] == 'Bebida':
    if qtd_estoque < minimo_bebidas:
        print(f'\tSolicitar {lista_produtos[item_escolhido]} á equipe de compras\n\tTemos apenas: {qtd_estoque} und em estoque')
    else:
        print(f'\tEstoque dentro do esperado \n\tTemos: {qtd_estoque} und do item: {lista_produtos[item_escolhido]}')

elif produtos[lista_produtos[item_escolhido]] == 'Limpeza':
    if qtd_estoque < minimo_limpeza:
        print(f'\tSolicitar {lista_produtos[item_escolhido]} á equipe de compras\n\tTemos apenas: {qtd_estoque} und em estoque')
    else:
        print(f'\tEstoque dentro do esperado \n\tTemos: {qtd_estoque} und do item: {lista_produtos[item_escolhido]}')