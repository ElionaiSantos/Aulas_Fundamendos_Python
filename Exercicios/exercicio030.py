# Crie o jogo pedra, papel, tesoura.

print('Jogo: Pedra, Papel, Tesoura')

jogador1 = input(' Jogador 1 escolha: pedra, papel ou tesoura\n--> ')
jogador2 = input(' Jogador 2 escolha: pedra, papel ou tesoura\n--> ')

if jogador1 == jogador2:
    print('Empate')

elif (jogador1 == 'tesoura' and jogador2 == 'papel') or\
    (jogador1 == 'papel' and jogador2 == 'pedra') or \
        (jogador1 == 'pedra' and jogador2 == 'tesoura'):
    print('O jogador 1 venceu')

elif (jogador2 == 'tesoura' and jogador1 == 'papel') or\
    (jogador2 == 'papel' and jogador1 == 'pedra') or \
        (jogador2 == 'pedra' and jogador1 == 'tesoura'):
    print('O jogador 2 venceu')

else:
    print('Jogada invalida')

