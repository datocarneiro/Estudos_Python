# ******************************************************************************************************
#                                               Minha SOLUÇÂO
# ******************************************************************************************************
def somar_elementos_da_lista(lista):

    for indice, valor in enumerate(lista):
        for indice_2, numero in enumerate(lista):
            try:
                if valor == lista[indice_2+1]:
                    continue
                soma = valor + lista[indice_2+1]
                if soma == soma_alvo:

                    mensagem = f'A soma de "({valor} e {lista[indice_2+1]})", é igual a Soma alvo =>"({soma_alvo})"'
                    return mensagem
                else: 
                    continue
            except:
                continue
    return 'Nehhum calculo é igual a Soma alvo'

soma_alvo = 11
lista = [3, 5, -4, 8, 11, 1, -2, 6]
print(somar_elementos_da_lista(lista))


# ******************************************************************************************************
#                                               Solução GPT 
# ******************************************************************************************************
def somar_elementos_da_lista(lista, soma_alvo):
    # Cria um conjunto para armazenar os complementos
    complementos = set()
    
    for numero in lista:
        complemento = soma_alvo - numero
        # Verifica se o complemento já foi visto
        if complemento in complementos:
            mensagem = f'A soma de ({numero} e {complemento}) é igual à Soma alvo => ({soma_alvo})'
            return mensagem
        # Adiciona o número atual ao conjunto de complementos
        complementos.add(numero)
    
    return 'Nenhum cálculo é igual à Soma alvo'

soma_alvo = 11
lista = [3, 5, -4, 8, 11, 1, -2, 6]
print(somar_elementos_da_lista(lista, soma_alvo))

# Uso de Conjunto: Utilizamos um conjunto (set) para armazenar os complementos necessários 
# para alcançar a soma alvo. Isso permite verificar em tempo constante 
# 𝑂(1) se o complemento já foi visto.

# Eliminação do Segundo Loop:
# Ao usar um conjunto, não precisamos de um segundo loop, o que reduz a complexidade de tempo de 
# 𝑂(𝑛2) para 𝑂(𝑛).

# Sem Exceções para Controle de Fluxo: 
# Eliminamos o uso de try e except para um fluxo de controle mais limpo e eficiente.

# Comentários e Legibilidade: 
# Usamos nomes de variáveis mais claros e adicionamos comentários para melhorar a legibilidade do código.
