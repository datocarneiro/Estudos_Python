
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

def formatar_cpf(cpf_formatado):
    # Formatar o CPF no padrão xxx.xxx.xxx-xx
    cpf_digitado = str(cpf_input)
    # cpf_formatado = f'{cpf_digitado[:9]}-{cpf_digitado[9:]}'
    cpf_formatado = f'{cpf_digitado[:9]}-{cpf_digitado[9:]}'
    
    return cpf_formatado

# Solicitar ao usuário que digite o CPF
while True:    
    try:
        cpf_input = int(input("Digite o CPF [apenas números]: "))
        # Formatando o CPF e exibindo o resultado
        cpf_formatado = formatar_cpf(cpf_input)
        print(f"CPF informado:... {cpf_formatado}")
        break
    except ValueError:
        print('Digite apenas Números Inteiros:')

#nove_digitos = cpf_formatado[:9]
nove_digitos = str(cpf_input)



resultado = 0
numero_regressivo1 = 10
for i in nove_digitos:
    resultado += int(i) * numero_regressivo1
    numero_regressivo1 -= 1

primeiro_digito = (resultado * 10) % 11 if (resultado * 10) % 11 <= 9 else 0
print(f'Validando o primeiro dígito:... {primeiro_digito}')

#############################################################################################################

# Calculo do segundo dígito do CPF
# CPF: 746.824.890-70
# Colete a soma dos 9 primeiros dígitos do CPF,
# MAIS O PRIMEIRO DIGITO,
# multiplicando cada um dos valores por uma
# contagem regressiva começando de 11

# Ex.:  746.824.890-70 (7468248907)
#    11 10  9  8  7  6  5  4  3  2
# *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
#    77 40 54 64 14 24 40 36  0 14

# Somar todos os resultados:
# 77+40+54+64+14+24+40+36+0+14 = 363
# Multiplicar o resultado anterior por 10
# 363 * 10 = 3630
# Obter o resto da divisão da conta anterior por 11
# 3630 % 11 = 0
# Se o resultado anterior for maior que 9:
#     resultado é 0
# contrário disso:
#     resultado é o valor da conta

# O segundo dígito do CPF é 0

#concatenando os 9 digitos + o primeiro dígito
dez_digitos = nove_digitos+str(primeiro_digito)
print(f'Dez dígitos:... {dez_digitos}')

resultado = 0
numero_regressivo2 = 11
for i in dez_digitos:
    resultado += int(i) * numero_regressivo2
    numero_regressivo2 -= 1

segundo_digito = (resultado * 10) % 11 if (resultado * 10) % 11 <= 9 else 0
print(f'Validando o segundo dígito:... {segundo_digito}')

resultado_cpf = dez_digitos + str(segundo_digito)
# resultado_cpf_formatado = formatar_cpf(resultado_cpf)
cpf_formatado = f'{resultado_cpf[:9]}-{resultado_cpf[9:]}'
print(cpf_formatado)

if 

