
'''limite_de_velocidade = 120

minimo_velocidade = 50

print('--- RADAR DE VELOCIDADE ---')

velocidade = int(input('----> '))

if velocidade > limite_de_velocidade:
        print('MULTADO')

elif velocidade < minimo_velocidade:
    print('Acelera moçoooo')

else:
    print('Boa Viagem')

print('Fim do programa')'''

'''print('--- Calculadora ---')
print('[ 1 ] – Tabuada')
print('[ 2 ] – Calculadora')
print('[ 3 ] – Fatorial')
print('[ 4 ] – Números primos')

opcao = input('---> ')

if opcao == '1':
    print('Escolheu tabuada.')

elif opcao == '2':
    print('Escolheu calculadora.')

elif opcao == '3':
    print('Escolheu fatorial.')

elif opcao == '4':
    print('Escolheu numeros primos.')

else:
    print('Numéro invalido.')
    
print('Fim do programa')'''

email = input('Digite o seu email: ')

if '@' in email and '.' in email:
    print('É um email')

else:
    print('Não é um email')