# Flíper é um tipo de jogo onde uma bolinha de metal cai por um labirinto de caminhos até chegar na parte de baixo do labirinto.
# A quantidade de pontos que o jogador ganha depende do caminho que a bolinha seguir. 
# O jogador pode controlar o percurso da bolinha mudando a posição de algumas portinhas do labirinto. 
# Cada portinha pode estar na posição 0, que significa virada para a esquerda, ou na posição 1 que quer dizer virada para a direita. 
# Considere o flíper da figura abaixo, que tem duas portinhas. 
#                                  (E)
#                                 [0][1]
#                                  /  \
#           Left = 0              /    \
#           Rigth = 1           (E)    (E)
#           Escolha = E       [0][1]  [0][1]
#                              /  \    /  \
#                             /    \  /    \
#                           (A)     (B)    (C) 

A = [0,0]
B = [[0,1], [1,0]]
C = [1,1]
lista = []
continuar = ''
while continuar != 'n':
    for i in range(2):
        posicao = int(input("Digite a opção entre [0 e 1]:     "))
        lista.append(posicao)
        if lista == A:
            print("Caminho A escolhido")
            break
        elif lista == B[0] or lista == B[1] :
            print("Caminho B escolhido")
            break
        elif lista == C:
            print("Caminho C escolhido")
            break
        else:
            print('Caminho não existe')
    lista.clear()
    print('*' *30)
    continuar = input('COntinuar? s(sim) | n(não): ')
