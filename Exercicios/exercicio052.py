#Crie um programa com um tuple com os 20
#Espanhol de Futebol. Depois mostre:


#b) Os últimos 4 classificados.
#c) Uma lista com as equipas por ordem alfabética.
#d) A posição da equipa Las Palmas.

equipas = (
    'Barcelona', 'Real Madrid', 'Atlético Madrid',
    'Atletic Bilbao', 'Villareal',  'Betis',
    'Celta Vigo', 'Rayo Val', 'Osasuna', 'Mallorca',
    'Real Sociedade', 'Valência', 'Getafe', 'Espanhol',
    'Alavés', 'Girona', 'Sevilla', 'Leganés', 'Las Palmas',
    'Valladoilid')

while True:
    print('--- Menu ---')
    print('[a] Os primeiros 5 classificados.')
    print('[b] Os últimos 4 classificados.')
    print('[c] Uma lista com as equipas por ordem alfabética.')
    print('[d] A posição da equipa Las Palmas.')
    print('[e] A sair ...')

    opcao = (input('Digite a sua opção: ')).lower()

    posicao = 0

    if opcao == 'a':
        print('\nOs primeiros 5 classificados são: ')
        for c in equipas[:5]:
            posicao += 1
            print(f'{posicao}º - {c}')

    elif opcao == 'b':
        print('Os últimos 4 classificados são: ')
        for c in equipas[-4:]:
            posicao += 1
            print(f'{posicao}º - {c}')

    elif opcao == 'c':
        print('\Equipas por ordem alfabeticas: ')
        for c in sorted(equipas):
            posicao += 1
            print(f'{posicao}º - {c}')


    elif opcao == 'd':
        for c in range (0, len(equipas)):
            if equipas[c] == 'Las Palmas':
                print(f'A equipa Las palmas encontra-se na posição {c + 1}º')


    elif opcao == 'e':
        print('A sair ...')
        break

    else:
        print('Tente novamente, uma opção valida')






