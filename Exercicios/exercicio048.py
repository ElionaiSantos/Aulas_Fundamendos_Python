#utilizar o while true e o for (0,10)
print('--- TABUADA 2.0 ---')

while True:

    numero = int(input('Digite um número: '))

    if numero <= 0:
        break

    for c in range(0, 10):
        print(f'{numero} x {c + 1} = {numero * (c + 1)}')