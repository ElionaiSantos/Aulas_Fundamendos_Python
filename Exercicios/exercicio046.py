#Crie um programa que leia vários
#números inteiros e que termine apenas
#quando o utilizador digitar a opção
#para parar. No final mostre quantos
#números o utilizador inseriu e qual a
#soma entre eles.

contador = 0
soma = 0

while True:
    numero = (input('Digite um número: '))
    if numero.lower() == 'parar':
        break
    soma += int(numero)
    contador += 1
    print(f'Você tentou  {contador} vezes')
    print(f'A soma dos numuros introduzidos é {soma}')





