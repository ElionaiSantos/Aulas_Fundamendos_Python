import random

qtd = int(input('Quantas chaves deseja gerar?\n'))

chaves = []

for c in range(qtd):
    numeros = random.sample(range(0, 50), 5)
    numeros.sort()

    estrelas = random.sample(range(0, 12), 2)
    estrelas.sort()

    chaves.append([numeros, estrelas])

print('\nChaves geradas: ')
for i, chave in enumerate(chaves, 1):
    print(f'Chave {i}: Números = {chave[0]} | Estrelas = {chave[1]}')
