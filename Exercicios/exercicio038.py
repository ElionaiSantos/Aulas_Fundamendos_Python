
frase = input('Digite um frase: ').replace(' ', '').lower()

frase_reverse = ''

tam = len(frase)

for c in range(tam, 0, -1):
    frase_reverse += frase[c-1]

if frase_reverse == frase:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')






'''frase = input('Digite uma frase: ').replace(' ', '').lower()
sem_espaco = ' '

tam = len(frase)

for c in range(tam, 0, -1):
    if c != ' ':
        sem_espaco += frase[c-1]

invertida = ' '
for i in range(len(sem_espaco) -1, -1, -1):
    invertida += sem_espaco[i]

if sem_espaco == invertida:
    print('A frase é um políndrono')
else:
    print('A frase não é um políndrono')'''

