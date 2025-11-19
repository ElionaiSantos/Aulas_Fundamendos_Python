#Crie um programa que leia um número de
#0 a 20 introduzido pelo utilizador.
#Depois deverá mostrar por extenso o
#número introduzido.

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')

num = int(input('Introduza um número entre 0 a 20: '))

while num < 0 or num > 20:
    num = int(input('Tente novamete.\nIntroduza um número entre 0 a 20: '))

print(f'O numero por extenso é {numero[num]}')
