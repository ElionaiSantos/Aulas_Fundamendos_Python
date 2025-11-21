Aluno = {}

Aluno['nome'] = input('Digite o nome do aluno: ')
Aluno['media'] = float(input('Digite a média do aluno: '))

if Aluno['media'] >= 9.5:
    Aluno['Situação'] = 'Aprovado'
else:
    Aluno['Situação'] = 'Reprovado'

for chave, valor in Aluno.items():
    print(f'{chave}, {valor}')


