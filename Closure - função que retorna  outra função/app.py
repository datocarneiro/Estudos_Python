variavel = []
def dentro(x):    
    numero = x
   
    def fora():
        print(f'fora: {globals()}')
        return numero
    return fora()

chamada1 = dentro(50)

print(chamada1)

#  Anotação:
# com a função locals(),
# podemos saber quais variavés estão diponíveis dentro de cada escopo

# verificar sobre variaveis livres tambem 