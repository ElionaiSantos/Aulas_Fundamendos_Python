'''import random

vitorias = 0

print('--- Par ou Ímpar ---')

while True:
    jogada = int(input('Digite um valor entre 0 e 5: '))
    if jogada > 5 or jogada < 0:
        print('Por favor escolha um valor entre 0 e 5 ')
        continue
    while True:
        jogada_pi = input('[ PAR OU IMPAR ]: ').strip().lower()
        if jogada_pi == 'par' or jogada_pi == 'impar':
             break
        else:
            print('Por favor digite ')

    CPU = random.randint(0,10)
    res = CPU + jogada

    elif res % 2 '''



