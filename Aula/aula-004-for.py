#range (inicio, fim e passo)
from time import sleep

'''for c in range(0, 100, 2):
    print(c)'''

'''for c in range(0, 10, 2):
    print(c + 1)'''

'''soma = 0

for c in range(0, 5):
    print(f'O valor da soma é {soma}')
    nota = float(input(f'Digite s {c + 1}ª nota: '))
    soma += nota # é o mesmo que soma = soma + nota

    print(soma/5)'''

numero = 7

for c in range(0,10):
    print(f'{numero} x {c +1} = {numero * (c + 1)}')
    input()