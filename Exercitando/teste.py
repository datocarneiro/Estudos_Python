
soma_alvo = 10
lista = [3, 5, -4, 8, 11, 1, -1, 6]
for i in range(0, len(lista)-1):
    for numero in lista:
        if lista[i] + numero == soma_alvo:
            print(f'{lista[i]} + {numero} é igual')
        else:
            print(f'{lista[i]} + {numero} não')s