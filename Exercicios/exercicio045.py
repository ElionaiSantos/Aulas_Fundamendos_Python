print('--- Sequência de Fibonacci ---')

antecessor = 0
atual = 1
sucessor = antecessor + atual

sequencia = int(input('Digite um valor inteiro: '))

if sequencia == 0:
    print('Inválido')
elif sequencia == 1: # se a sequencia for 1 ele mostra o primeiro valor da sequencia
    print(sucessor)
elif sequencia == 2: # se a sequencia for 2 ele mostra o segundo valor da sequencia
    print(f'{antecessor} -> {atual}')
else:
    print(f'{antecessor} -> {atual}', end=' ')

    sequencia = sequencia - 2 # libertamos 2 valores da sequencia porque na linha anterior 2 ja foram exibidos

    while sequencia >= 1:
        sucessor = antecessor + atual
        print(f'-> {sucessor}', end=' ')
        antecessor = atual
        atual = sucessor


'''print('--- Sequência de Fibonacci ---')

Numero = int(input('Digite um número inteiro: '))

if Numero <= 0:
    print('Por favor, digite um número maior que 0.')
else:
    fib1, fib2 = 0, 1
    contador = 0

    print(f'Os {Numero} primeiros elementos da sequência de Fibonacci são:', end=' ')

    while contador < Numero:
        print(fib1, end=' ')
        fib1, fib2 = fib2, fib1 + fib2
        contador += 1

    print()  # pular linha no final'''
