import random
from sys import exit
#Joguinho de adivinhão usando laço de repetição
print('----------------')
print('ACERTE O NÚMERO!')
print('----------------')

inicio = True
while True:
    if(inicio):
        vidas = 5
        numero = random.randint(1, 50)
        meuChute =int(input("Chute um número: "))
        inicio = False

    if vidas > 0:
        if meuChute == numero:
            print("Você acertou")
            break
        elif meuChute > numero:
            print("Seu chute foi maior que o número.")
            vidas -= 1
            meuChute = int(input("Chute um número: "))
            continue
        elif meuChute < numero:
            print("Seu chute foi menor que o número.")
            vidas -= 1
            meuChute = int(input("Chute um número: "))
            continue

    elif vidas == 0:
        while True:
            decisao = input('voce perdeu! Quer tentar novamente? Digite "mais" para jogar ou digite "sair" para encerrar o jogo: ')
            if decisao == 'mais':
                inicio = True
                break
            elif decisao == 'sair':
                exit()
            elif decisao != 'mais' or decisao != 'sair':
                print("Nao entendi o que você digitou...")
                continue










