from time import sleep
import math

print('-', end='')
sleep(0.5)
print('-', end='')
sleep(0.5)
print('-', end='')
sleep(0.5)
print('Calculadora do Índice de Massa Corporal (IMC)', end='')
print('-', end='')
sleep(0.5)
print('-', end='')
sleep(0.5)
print('-', end='')

sleep(0.5)
peso = float(input('\n\nDigite o seu peso em quilogramas (Kg)\n--> '))
sleep(0.1)
altura = float(input('\nDigite a sua altura em metros (m)\n--> '))

IMC = (peso / (altura**2))

if IMC < 18.5:
    print(f'O seu IMC é de {IMC:.2f}  e está a baixo do peso')
elif IMC >= 18.5 and IMC <= 24.9:
    print(f'O seu IMC é de {IMC:.2f}  e está com o peso normal')
elif IMC >= 25.0 and IMC <= 29.9:
    print(f'O seu IMC é de {IMC:.2f} e está com o sobrepeso')
elif IMC >= 30.0 and IMC <= 34.0:
    print(f'O seu IMC é de {IMC:.2f}  e está com obesidade grau 1')
elif IMC >= 35.0 and IMC <= 39.9:
    print(f'O seu IMC é de {IMC:.2f}  e está com o obesidade grau 2')
else:
    print(f'O seu IMC é de {IMC:.2f} e está com o obesidade grau 3 (obesidade mórbida)')

