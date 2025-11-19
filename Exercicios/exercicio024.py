limite_de_velocidade = 80

valor_da_multa = 100

print('--- RADAR DE VELOCIDADE ---')

velocidade = int(input('----> '))

multa = valor_da_multa + (7*velocidade)

if velocidade > limite_de_velocidade:
        print(f'MULTADO, o valor é: ', (multa),'€')

elif velocidade <= limite_de_velocidade:
    print('NÃO MULTADO')

else:
    print('Boa Viagem')

print('Fim do programa')