
# Calculo do primeiro dígito do CPF
#     CPF: 746.824.890-70
#     Colete a soma dos 9 primeiros dígitos do CPF
#     multiplicando cada um dos valores por uma
#     contagem regressiva começando de 10

#     Ex.:  746.824.890-70 (746824890)
#                         10  9  8  7  6  5  4  3  2
#                       *  7  4  6  8  2  4  8  9  0
#     Resultado da conta: 70  36 48 56 12 20 32 27 0

#     Somar todos os resultados: 
#     70+36+48+56+12+20+32+27+0 = 301
#     Multiplicar o resultado anterior por 10
#     301 * 10 = 3010
#     Obter o resto da divisão da conta anterior por 11
#     3010 % 11 = 7
#     Se o resultado anterior for maior que 9:
#         resultado é 0
#     contrário disso:
#         resultado é o valor da conta

#     O primeiro dígito do CPF é 7

# 75532282064
# 602.440.980-00 , 755.322.820-64
def formatar_cpf(cpf_formatado):
    # Formatar o CPF no padrão xxx.xxx.xxx-xx
    cpf_digitado = str(cpf_input)
    cpf_formatado = f'{cpf_digitado[:9]}-{cpf_digitado[9:]}'
    
    return cpf_formatado

# Solicitar ao usuário que digite o CPF
while True:    
    try:
        cpf_input = 74682489070 # int(input("Digite o CPF [apenas números]: "))
        # Formatando o CPF e exibindo o resultado
        cpf_formatado = formatar_cpf(cpf_input)
        print(f"CPF informado: {cpf_formatado}")
        break
    except ValueError:
        print('Digite apenas Números Inteiros:')

cpf_lista = []
for i in cpf_formatado[:9]:
    cpf_lista.append(i)
print(cpf_lista)

#conta multiplicação 
resultado = []
numero_para_multiplicar = 10
for i in cpf_lista:
    i = int(i) * numero_para_multiplicar
    numero_para_multiplicar -= 1
    resultado.append(i)
print(resultado)
soma = sum(resultado)
print(soma)
resultado_mul2 = soma * 10
print(f'Multiplicar o resultado anterior por 10:......{resultado_mul2}')
resto = resultado_mul2 % 11
print(f'Obter o resto da divisão da conta anterior por 11:....... {resto}')
