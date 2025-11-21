from random import randint

qtdJogadores = int(input('Digite quantos jogadores vão jogar: '))
jogadores = {}

for c in range(qtdJogadores):
    nome = input(f'Digite o nome do {c+1}º jogador: ')
    jogada = randint(1, 6)

    jogadores[nome] = jogada

auxiliar = jogadores.copy()
ranking = list()

while len(auxiliar) > 0:
    maior_jogador = ''
    maior_valor = 0

    for jogador, jogada in auxiliar.items():
        if jogada > maior_valor:
            maior_jogador = jogador
            maior_valor = jogada
    ranking.append((maior_jogador, maior_valor))
    del auxiliar[maior_jogador]

print('\n--- RANKING FINAL ---')
for i, (nome, valor) in enumerate(ranking):
    print(f' {i + 1}º Lugar: O jogador {nome} tirou o valor {valor}')
