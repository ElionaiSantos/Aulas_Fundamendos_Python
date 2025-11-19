# Lê a frase escrita
escreva_uma_frase = input('Escreva uma frase: ')

# Quantas vezes aparece a letra “A”;
contar_letra_a = escreva_uma_frase.count('a',0, )

# Em que posição aparece a primeira vez;
posicao_primeira_letra_a = escreva_uma_frase.find('a') + 1

#Em que posição aparece a última vez.
posicao_ultima_letra_a = escreva_uma_frase.rfind('a') +1

print(f'A letra a é repetida: {contar_letra_a}', 'vezes')
print(f'A primeira posição da letra a é: {posicao_primeira_letra_a}')
print(f'A ultima posição da letra a é: {posicao_ultima_letra_a}')