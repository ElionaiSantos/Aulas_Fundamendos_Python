
qtd_pares = 0

for c in range(0, 10):
    nota = float(input(f'Digite a {c + 1}ª nota: '))
    if nota % 2 == 0:
        '''print('O valor introduzido é par')'''
        qtd_pares += 1
        print(qtd_pares)


