import random
from time import sleep

numero_pc = random.randint(0,7)
#numero_pc = 6

print('-', end='')
sleep(0.5)
print('-', end='')
sleep(0.5)
print('-', end='')
sleep(0.5)
print('Deixe Pensar num Número e Tente Adivinhar', end='')
print('-', end='')
sleep(0.5)
print('-', end='')
sleep(0.5)
print('-', end='')


sleep(0.5)
palpite = int(input('\n\nDigite um número entre 0 à 7\n---> '))

if numero_pc == palpite:
    print('Você acertou')

else:
    print('Você errou')
print(f'Eu pensei em {numero_pc} e tu jogaste {palpite}')
