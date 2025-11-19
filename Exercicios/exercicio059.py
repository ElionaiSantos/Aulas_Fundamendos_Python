lista = []
for c in range(0, 10):
    numero = int(input(f'Digite o {c + 1} numero: '))
    lista.append(numero)

pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

        print(lista)
        print(pares)
        print(impares)