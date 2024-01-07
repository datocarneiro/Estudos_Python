# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

# crie uma função fala se um numero é par ou impar 
# retorna se o numerp é par ou impar

def calculo(*args):
    global total
    total= 0
    for i in args:
        total *= i
        print(total)
    return total

print(1*2*3)

calculando = calculo(*1,2,3)
print(calculando)