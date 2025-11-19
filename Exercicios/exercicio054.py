# Lê 4 valores e guarda-os numa tuple
valores = (
    int(input('Digite o 1º valor: ')),
    int(input('Digite o 2º valor: ')),
    int(input('Digite o 3º valor: ')),
    int(input('Digite o 4º valor: '))
)

conta_7 = 0
for c in valores:
    if c == 7:
        conta_7 += 1

if conta_7 > 0:
    print('O número 7 apareceu', conta_7, 'vez(es).')
else:
    print('O número 7 não apareceu.')

posicao_5 = -1
for c in range(len(valores)):
    if valores[c] == 5:
        posicao_5 = c + 1
        break

if posicao_5 != -1:
    print('O número 5 foi digitado na posição', posicao_5)
else:
    print('O número 5 não foi digitado.')

# c) Mostrar os números pares
pares = []
for c in valores:
    if c % 2 == 0:
        pares.append(c)

if len(pares) > 0:
    print('Números pares digitados:', pares)
else:
    print('Nenhum número par foi digitado.')
