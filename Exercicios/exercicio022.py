# Lê o nome completo
nome_completo = input('Digite o seu nome completo: ')

# Dividindo o nome em parte

partes = nome_completo.split()

# primeiro nome
primeiro_nome = partes[0]

# ultimo nome
ultimo_nome = partes[-1]

#Mensagem do registo
print(f'Olá {primeiro_nome}', 'o seu registo está completo' )

# Criação do email, o '0' indica a primeira posicao da primeira palavra
email = f'{primeiro_nome[0].lower()}.{ultimo_nome.lower()}@empresa.pt'
print(f'O seu email é {email}')
