print('--- Calculadora ---')
print('[ 1 ] – Tabuada')
print('[ 2 ] – Calculadora')
print('[ 3 ] – Números pares')
print('[ 4 ] – Sair')

opcao = input('---> ')

if opcao == '1':
    print('Escolheu tabuada.')
    num1 = int(input('Introduza um valor: '))

    print('A tabuada do valor introduzido é: ')
    print(f'{num1} x 1 = {num1 * 1}')
    print(f'{num1} x 2 = {num1 * 2}')
    print(f'{num1} x 3 = {num1 * 3}')
    print(f'{num1} x 4 = {num1 * 4}')
    print(f'{num1} x 5 = {num1 * 5}')
    print(f'{num1} x 6 = {num1 * 6}')
    print(f'{num1} x 7 = {num1 * 7}')
    print(f'{num1} x 8 = {num1 * 8}')
    print(f'{num1} x 9 = {num1 * 9}')
    print(f'{num1} x 10= {num1 * 10}')
    print(f'{num1} x 11= {num1 * 11}')
    print(f'{num1} x 12= {num1 * 12}')

elif opcao == '2':
    print('Escolheu calculadora.')

    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    operaçao = input('[ + - * / ] ')

    if operaçao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')

    elif operaçao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')

    elif operaçao == '*':
        print(f'{num1} * {num2} = {num1 * num2}')

    elif operaçao == '/':
        print(f'{num1} / {num2} = {num1 / num2}')

    '''calculo = input('Digite o calculo: ').strip().replace(' ', '')

    if '+' in calculo:
        pos = calculo.find('+') # encontro o indice do sinal
        num1 = int(calculo[:pos]) # tudo a esquerda do sinal
        num2 = int(calculo[pos +1:]) # tudo a direita do sinal
        print(f'{num1} + {num2} = {num1 + num2}')

    elif '-' in calculo:
        pos = calculo.find('-')  # encontro o indice do sinal
        num1 = int(calculo[:pos])  # tudo a esquerda do sinal
        num2 = int(calculo[pos + 1:])  # tudo a direita do sinal
        print(f'{num1} - {num2} = {num1 - num2}')

    elif '*' in calculo or 'x' in calculo:
        pos = calculo.find('*')  # encontro o indice do sinal
        pos = calculo.find('x')  # encontro o indice do sinal
        num1 = int(calculo[:pos])  # tudo a esquerda do sinal
        num2 = int(calculo[pos + 1:])  # tudo a direita do sinal
        print(f'{num1} x {num2} = {num1 * num2}')

    elif '/' in calculo:
        pos = calculo.find('/')  # encontro o indice do sinal
        num1 = int(calculo[:pos])  # tudo a esquerda do sinal
        num2 = int(calculo[pos + 1:])  # tudo a direita do sinal
        print(f'{num1} / {num2} = {num1 / num2}')
        if num2 == 0:
            print('Não é possível dividir por zero')'''


elif opcao == '3':
        print('Escolheu números pares.')
        numero = int(input('Digite um numero: '))

        if numero % 2 == 0:
            print('O numero é par')

        else:
            print('O número é ímpar')

elif opcao == 4:
        print('Sair...')

else:
    print('Opção invalida')


print('Fim do programa')

