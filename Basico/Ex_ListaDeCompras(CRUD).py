
# Faça uma lista de comprar com listas
# O usuário deve ter a possibilidade de
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com 
# erros de índices inexistentes na lista.

lista = []
while True:
    opcoes = input('[l]istar [i]nserir [a]pagar: ')
    if opcoes == 'l':
        if len(lista) == 0:
            print('lista vazia')
            continue
        else:
            for i, v in enumerate(lista):
                print(i, v)
    elif opcoes == 'i':
        inserir_item = input('item: ')
        lista.append(inserir_item)            
    elif opcoes == 'a':
        if len(lista) == 0:
            print('lista vazia')
            continue
        else:
            while True:
                try:
                    numero_digitado = int(input('digite o índice: '))
                    del lista[numero_digitado]
                    break
                except ValueError:
                    print('O valor digitado não é um Número')
                except IndexError:
                    print('Não ha o indice na lista')            
                except Exception:
                    print('Erro desconhecido')    
    else: 
        print('opção invalida')  
