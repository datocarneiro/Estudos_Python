# copy, sorted, produtos.sort
# Exercícios
import copy

# Aumente os preços dos produtos a seguir em 10%
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},  #0
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

for produto in produtos:
    precoProduto = produto.get('preco')
    porcentagemAumento = precoProduto * 0.10
    precoProduto += porcentagemAumento
    produto.update({'preco': precoProduto})

# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
lista = []
for i in novos_produtos:
    lista.append(i['nome'])
print(sorted(lista))
    



    # for v in i.values():
    #     ordenar = sorted(v)
    #     print(ordenar)

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)