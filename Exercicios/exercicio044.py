print(' --- Cálculo do Fatorial ---')

numero = int(input('Digite um número: '))

fatorial = 1
contador = 1  # começa pelo 1

print(f'{numero}! = ', end=' ')

if numero == 0:
    print('1')  # definição matemática
elif numero < 0:
    print('Não existe fatorial negativo')
else:
    while contador <= numero:
        print(f'{contador}', end=' ')
        if contador < numero:
            print('x', end=' ')
        fatorial *= contador
        contador += 1
    print(f'= {fatorial}')

numero = int(input('Digite um numero: '))

if numero == 0 or numero == 1:
    print(f'O fatorial de {numero} é 1.')
