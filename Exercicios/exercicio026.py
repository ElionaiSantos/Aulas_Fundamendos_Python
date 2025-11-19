#Crie um programa que leia 5 notas de um aluno e calcule a sua média.
num1 = float(input('Introduza o primeiro valor: '))
num2 = float(input('Introduza o segundo valor: '))
num3 = float(input('Introduza o terceiro valor: '))
num4 = float(input('Introduza o quarto valor: '))
num5 = float(input('Introduza o quinto valor: '))

media = (num1 + num2 + num3 + num4 + num5) / 5

print('O valor da média é: ',media,)

if media >= 9.5:
        print(f'Aprovado com media de {media:.2f} valores')

elif media > 8 and media < 9.5:
    print('Recuperação')

elif media < 8:
    print('Reprovado')

else:
    print('Consultar o professor')