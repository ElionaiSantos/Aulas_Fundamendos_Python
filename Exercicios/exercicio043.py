num1 = float(input('Introduza o primeiro valor: '))
num2 = float(input('Introduza o segundo valor: '))
num3 = float(input('Introduza o terceiro valor: '))

while True:
    print('\n--- MENU ---')
    print('[ 1 ] - Somar')
    print('[ 2 ] - Multiplicar?')
    print('[ 3 ] - Maior.')
    print('[ 4 ] - Novos Números.')
    print('[ 5 ] - Sair do Programa.')

    opcao = (input('--> '))


    if opcao == '1':
        soma = num1 + num2 + num3
        print(f'O resultada da soma é {num1} + {num2} + {num3} = {soma}')

    elif opcao == '2':
        produto = num1 * num2 * num3
        print(f'O produto dos valores é  {num1} * {num2} * {num3} = {produto}')

    elif opcao == '3':
        maior = max(num1, num2, num3)
        print(f'O maior valor entre {num1} , {num2} , {num3} é o {maior}')

    elif opcao == '4':
        print('Insira novos números!\n')
        num1 = float(input('Introduza o primeiro valor: '))
        num2 = float(input('Introduza o segundo valor: '))
        num3 = float(input('Introduza o terceiro valor: '))

    elif opcao == '5':
        print('Saindo do programa...')
        break  # volta para o while externo para pedir novos números

    else:
        print('Opção inválida! Tente novamente.')











