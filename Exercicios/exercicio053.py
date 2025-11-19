# Crie um programa que gere 5 números
# aleatórios dentro de um tuple. Depois
# mostra a listagem de números gerados, o
# menor e o maior.

import random

# Gera 5 números aleatórios e guarda-os numa tuple
numeros = (
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100)
)

print('Números gerados:', numeros)

# Inicializa o menor e maior com o primeiro número
menor = numeros[0]
maior = numeros[0]

# Percorre os restantes números para encontrar o menor e o maior
for n in numeros[1:]:
    if n < menor:
        menor = n
    if n > maior:
        maior = n

print('Menor número:', menor)
print('Maior número:', maior)
