
while True:
    print('--- MENU ---')
    print('[1] Escada à Esquerda')
    print('[2] Escada à Direita')
    print('[3] Árvore de Natal')
    print('[4] Forma de X')
    print('[5] Sair')

    opcao = int(input('Digite a sua opção: '))

    if opcao == 1:
        print('\n--- Escada à Esquerda ---')
        tamanho = 5

        for c in range(0, tamanho):
            print('*' * (c + 1))

    elif opcao == 2:
        print('\n--- Escada à Direita ---')
        tamanho = 5

        for c in range(0, tamanho):
            espacos = ' ' * (tamanho - (c + 1))
            asteriscos = '*' * (c + 1)
            print(espacos + asteriscos)

    elif opcao == 3:
        print('\n--- Árvore de Natal ---')
        altura = 5
        largura_maxima = (altura * 2) - 1

        for c in range(0, altura):
            folhas = '*' * (2 * (c + 1) - 1)
            espacos = ' ' * (altura - (c + 1))
            print(espacos + folhas + espacos)

    elif opcao == 4:
        print('\n--- Forma de X ---')
        tamanho = 5
        for c in range(0, tamanho):
            linha = ''
            for i in range(0, tamanho):
                if c == i or c + i == tamanho - 1:
                    linha += '*'
                else:
                    linha += ' '
            print(linha)

        print()

    elif opcao == 5:
        print('A sair...')
        break

    else:
        print('Opção inválida. Por favor, escolha um número de 1 a 5.')