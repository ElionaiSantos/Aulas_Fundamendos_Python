# Lê o nome completo da pessoa
nome_completo = input('Digite o seu nome completo: ')

# Nome em maiúsculas
nome_maiusculo = nome_completo.upper()

# Nome em minúsculas
nome_minusculo = nome_completo.lower()

# Quantidade de letras sem considerar espaços
qtd_letras_sem_espaco = (len(nome_completo.replace(' ', '')))

# Quantidade de letras no primeiro nome
primeiro_nome = nome_completo.split()[0]
letras_primeiro_nome = len(primeiro_nome)

print(f'Nome em MAÍUSCULA: {nome_maiusculo}')
print(f'Nome minusculo: {nome_minusculo}')
print(f'Quantidade de letras sem espaço: {qtd_letras_sem_espaco}')
print(f'Quantidades de letras do primeiro nome: {primeiro_nome}', {letras_primeiro_nome})
