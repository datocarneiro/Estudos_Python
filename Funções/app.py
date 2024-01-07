x = 300
def local1():
    x=10
    print(f'x local 1 = {x}')
    def local2():
        x=20
        print(f'x local 2 = {x}')
    # chamando a função local2
    local2()
# x nesse caso ESTA acessivel fora das funções
print(f'x global = {x}') 
# chamando a função local 1
local1()
print(f'x global apos função = {x}') 
######################################################################
# Resultado:  x local 1 = 10
#             x local 2 = 100