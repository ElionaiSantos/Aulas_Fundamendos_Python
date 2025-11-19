# Tuple com nomes de jogos e preços (alternados)
jogos = (
    'Minecraft', 19.99,
    'FIFA 25', 69.90,
    'The Witcher 3', 29.99,
    'GTA V', 24.50,
    'Fortnite ', 9.99)

print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
print(f'{"Jogo": <33} Preço')
print('-' * 40)

# Percorre a tuple de 2 em 2 (nome e preço)
for c in range(0, len(jogos), 2):
    nome = jogos[c]
    preco = jogos[c + 1]
    print(f'{nome:.<30} €{preco:>7.2f}')

print('-' * 40)
