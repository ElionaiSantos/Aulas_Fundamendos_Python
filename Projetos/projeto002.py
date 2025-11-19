from time import sleep

print('-', end='')
sleep(0.2)
print('-', end='')
sleep(0.2)
print('-', end='')
sleep(0.2)
print('Boas Vindas ao Nosso Programa', end='')
print('-', end='')
sleep(0.2)
print('-', end='')
sleep(0.2)
print('-', end='')

sleep(0.1)
print('\nFaça o seu registo')
username_in = input('usarname: ').strip()
email_in = input('Email: ').strip()
#verificação do email
if email_in.count('@') == 0 and email_in.count('.') == 0:
    print('Email invalido, tente novamente.')
    print('\nFaça o seu registo')
    username_in = input('username: ').strip()
    email_in = input('Email: ').strip()

password_in = input('Password: ').strip()
sleep(0.5)
print('Criando o seu perfil', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(1)
print('\nRegisto efetuado com sucesso, vamos reencaminhar para o login.\n', end='')
sleep(1)
# 4 -
print(' --- Menu --- ')
print('[1] - Login')
print('[2] - Sair')
opcao = input('--> ').strip().lower()
# 5- validação do menu
if opcao == 'login' or opcao == '1':
    sleep(0.1)
    print(' --- BEM VINDO --- ')
    username = input ('Username: ').strip()
    email = input('Email: ').strip()
    password = input('Password: ').strip()
    if username == username_in and email == email_in and password == password_in:
        print('Login efetuado com sucesso', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
    else:
        print('Username, password ou email não coincidem com registado, tente novamente.')
        username = input('Username: ').strip()
        email = input('Email: ').strip()
        password = input('Password: ').strip()
        if username == username_in and email == email_in and password == password_in:
            print('Login efetuado com sucesso')
        else:
            print('Username, password ou email não coincidem com registado, conta bloqueada.')

elif opcao == 'sair' or '2':
    print('Obrigado por utilizar o nosso programa, tenha um bom dia')

else:
    ('Opção invalida')
