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
import os 

######################################################################

# palavraSecreta = 'carro'
# continuar = "s"
# tentativas = 0
# while continuar=="s":
#     tentativas+=1
#     try:
#         letra = input('Digite uma letra: ')
#         if continuar == "s":
#             if letra in palavraSecreta:
#                 print(f'a letra digitada .... "{letra.upper()}" ... contém na palavra secreta')
#                 continuar = input(f' deseja continuar? [S]sim: ')
#             else:    
#                 quantidadeCaracteres = '*'*(len(palavraSecreta)-1)
#                 print(f'*{quantidadeCaracteres}')
#                 continuar = input(f'total de tentativas = {tentativas}, deseja continuar? [S]sim: ')
#     except:
#         break
# print(f'o total de tentativas foi: {tentativas}')

# print('voce encerrou o programa')


######################################################################

palavra_secreta = 'carro'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0





