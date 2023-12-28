"""Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário."""

palavraSecreta = 'carro'
continuar = "s"
tentativas = 0
while continuar=="s":
    tentativas+=1
    try:
        letra = input('Digite uma letra: ')
        if continuar == "s":
            if letra in palavraSecreta:
                print(f'a letra digitada .... "{letra.upper()}" ... contém na palavra secreta')
                continuar = input(f' deseja continuar? [S]sim: ')
            else:
                print("*")
                continuar = input(f'total de tentativas = {tentativas}, deseja continuar? [S]sim: ')
    except:
        break
print('voce encerrou o programa')



