#Crie um programa que leia várias notas
#introduzidas pelo utilizador. No final
#mostre quantas notas o utilizador
#inseriu, qual a média entre elas e
#qual a maior e a menor nota.

contador = 0
soma = 0

while True:
    numero = float(input(f'Digite a {contador + 1}ª nota [parar]: '))
    if numero.lower() == 'parar':
        break
    soma += int(numero)
    contador += 1
    print(f'Você tentou  {contador} vezes')
    print(f'A soma dos numuros introduzidos é {soma}')