# Desenvolva um programa que faça 3
# perguntas ao utilizador e apenas
# aceite como resposta “V” ou “F”. Caso
# esteja errado, peça para repetir a
# resposta até ter um valor correto.

resposta = ''
print('o céu é azul?')
while resposta != 'V' and resposta != 'F':
    resposta = input('[V / F]: ').strip().upper()
    if resposta == 'V':
        print('Acertou! Vamos à proxima')
    elif resposta == 'F':
        print('Errouuu!')
    else:
        print('Resposta invalida')

resposta = ''
print('O palmeiras tem mundial?')
while resposta != 'V' and resposta != 'F':
    resposta = input('[V / F]: ').strip().upper()
    if resposta == 'V':
        print('Errouuu!')
    elif resposta == 'F':
        print('Acertou! Vamos à proxima!')
    else:
        print('Resposta invalida')

print('O formador é o Ricardo?')
while True: # ou resposta != 'V' and resposta != 'F':
    resposta = input('[V / F]: ').strip().upper()
    if resposta == 'V':
        print('Acertou! Fim')
        break
    elif resposta == 'F':
        print('Errou!')
    else:
        print('Resposta invalida')