'''Crie um programa que tenha uma função
chamada area() que receba as dimensões
de um terreno e mostre a área do
terreno.'''

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A aréa do terreno {largura} x {comprimento} é de {a} m²')

print('Calculo da Aréa do terreno')
larg = float(input('largura (m): '))
comp = float(input('Comprimento (m): '))

area(larg, comp)