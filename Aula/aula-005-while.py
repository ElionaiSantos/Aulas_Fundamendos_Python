# Contador que vai de 1 até 10

'''contador = 1
while contador <= 10:
    print(contador) # se ele sempre for menor que 10 vai rolar infinitamente
    contador += 1 # por isso incrementamos o contador + 1

# Contador que vai de 10 até 0
contador = 10
while contador >= 0:
    print(contador) # se ele sempre for maior que 0 vai rolar infinitamente
    contador -= 1 # por isso incrementamos o contador - 1

    # crie um programa que some todos os utilizadores
    # Quantos
soma = 0
numero = ''
while numero != 0:
    numero = int(input('Digite um numero: '))
    soma += numero
print(soma)

# Eu quero criar um programa que peça o genero de uma pessoa
# Apenas aceita como resposta "M" ou "F"
#se o utilizador

genero = ''

while genero != 'M' and genero != 'F': # se eu colocar o indice [0] devo dar um espaço entre as aspas' '
    genero = input('Digite o seu género: ').strip().upper()'''

# Quero criar um menu onde o utilizador pode escolher 3 opções
# Escrever "olá", "tudo bem?", sair do programa

'''opcao = '''

'''while True: # posso colocar o True vai dar no mesmo (pcao != 3)
    print('--- MENU ---')
    print('[ 1 ] - Olá')
    print('[ 2 ] - Tudo bem?')
    print('[ 3 ] - Sair do programa.')
    opcao = int(input('--> '))

    if opcao == 1:
        print('Olá')
    elif opcao == 2:
        print('Tudo bem?')
    elif opcao == 3:
        print('Sair do programa')
        break
    else:
        print('opção inválida')'''

# Contagem de 0 até 1000

'''contador = -1
while True:
    contador += 1
    print(contador)

    if contador == 1000:
        break'''