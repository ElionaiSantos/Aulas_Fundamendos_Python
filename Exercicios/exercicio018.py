from time import sleep

print('---Calculadora do carro alugado---\n\n')
sleep(2)
num1 = float(input('Qual é a quantidade de quilometros (Km) percorridos pelo carro alugado?\n--> '))
num2 = int(input('Qual é a quantidade de dias que alugaste o carro?\n--> '))

valor_a_pagar = (num2 * 60) + (num1 * 0.456)

sleep(1)
print('O valor total a pagar é: ',valor_a_pagar, '€', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')