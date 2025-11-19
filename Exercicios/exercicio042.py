import random
from time import sleep

numero_pc = random.randint(0,10)
#numero_pc = 6

print(' --- Deixe Pensar num Número e Tente Adivinhar --- ')

sleep(0.2)
palpite = ''
qtd_palpite = 0
'''print(numero_pc)'''
while True:
    palpite = int(input('\nDigite um número entre 0 à 10\n---> '))
    if palpite == numero_pc:
        print(f'Você acertou! O número secreto era {numero_pc}')
        print(f'Precisaste de {qtd_palpite} tentativas')
        break

    elif palpite >= numero_pc:
        print('Você errou, tente um numero mais a baixo.')
    else:
        print('Você errou, tente um numero mais a cima.')

    if palpite >= qtd_palpite:
        qtd_palpite += 1
        print(f'{qtd_palpite}ª tentativa')
