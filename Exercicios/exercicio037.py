
numero = int(input('Digite um número inteiro: '))
divisores = 0

for c in range(0, numero):
    if numero % (c + 1) == 0:
        divisores += 1

if divisores == 2: # o resto zero só aconteceu duas vezes
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')