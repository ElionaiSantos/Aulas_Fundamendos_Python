from math import fsum
notas = list()

'''for c in range(0, 5):
    nota = float(input(f'Digite a {c + 1}ª nota: '))

    notas.append(nota)

media = fsum(notas) / len(notas)

print(f'{media:.2f}')

nomes = ['Nádia', 'Júlia', 'Alexandra']
print(nomes)

nomes.append('João')
print(nomes)

nomes.insert(0, 'Luana')
print(nomes)

nomes.pop(2)
print(nomes)'''

series = list()

print('Insere o teu top 5 de series')
for c in range(0, 5):
    serie = input(f'{c + 1}ª --> ')
    series.append(serie)
print(series)

while True:
    print('1 - Inserir novo top 5')
    print('2 - Substituir serie')
    print('3 - Mostrar top 5')
    print('4 - Sair...')

    opcao = int(input('---> '))

    match opcao:
        case 1:
            print('Insere o teu top 5 de series')
            for c in range(0, 5):
                serie = input(f'{c + 1}ª ---> ')
                series.append(serie)

        case 2:
            print('Substituir serie')
            nova_serie = input('Digite a nova serie: ')
            serie_remover = input('Digite a serie a remover: ')

            indice_serie_remover = series.index(serie_remover)

            series[indice_serie_remover] = nova_serie
            print('Serie alterada com sucesso')

        case 3:
            print('Insere o teu top 5 de series') 
            for c in range(0, 5):                 
                serie = input(f'{c + 1}ª ---> ')  
                series.append(serie)              

