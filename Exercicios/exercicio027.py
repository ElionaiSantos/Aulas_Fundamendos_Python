# Crie um programa que leia dois números inteiros e compare-os da seguinte forma:

num1 = int(input('Introduza o primeiro valor: '))
num2 = int(input('Introduza o segundo valor: '))

if num1 > num2:
    print(f'O {num1} é maior que o {num2}')

elif num1 < num2:
    print(f'O {num1} é menor que o {num2}')

else:
    print(f'Os numeros são iguais')