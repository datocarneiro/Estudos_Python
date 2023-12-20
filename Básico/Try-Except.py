'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
# Exemplo:
# numero = int(A)
# print(numero)

# O erro irá acontecer porque a não é um inteiro
# Traceback (most recent call last):
#   File "c:\Users\Dato\Documents\REPOSITÓRIO\Estudos-Python\Básico\Try-Except.py", line 7, in <module>
#     numero = int(a)
#                  ^
# NameError: name 'a' is not defined

while True:
    try: # tentar
        # tenta execultar o codigo se encontrar um erro dentro do try pula imediatamente para o except
        numero = int(input("Digite um número:"))
        print(f"O número informado foi: {numero} ")
    except:
        print(f"{numero}, isso não é um número")