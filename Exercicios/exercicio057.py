

numeros = []
contador = 0

while contador < 10:
    for c in range(0, 10):
        numero = int(input(f'Digite o {c + 1}º valor: '))
        if numero not in numeros:
            numeros.append(numero)
        else:
            print(f'O valor {numero} ja se encontra na lista')

    numeros.sort(reverse=True)
    for numero in numeros:
        print(f'{numero} -> ', end='')
        break