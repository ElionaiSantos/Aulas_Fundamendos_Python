from random import randint

qtdJogadores = int(input('Digite quantos jogadores vão jogar: '))
jogadores = {}

for c in range(qtdJogadores):
    nome = input(f'Digite o nome do {c+1}º jogador: ')
    jogada = randint( 1, 6)

    jogadores[nome] = jogada
