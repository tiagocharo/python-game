import random

def play():
    print("===========================================")
    print("BEM-VINDO AO JOGO DA ADIVINHAÇÃO DE NÚMEROS")
    print("===========================================\n")

    choose = print('Escolha seu nível:')
    level = print('(1) DIFÍCIL || (2) MÉDIO || (3) FÁCIL \n')
    define_level = int(input('Defina o nível: '))
    
    if define_level == 1:
        total_try = 5
    elif define_level == 2:
        total_try = 10
    else:
        total_try = 20

    print('Você tem {} tentativas\n'.format(total_try))
    secret_number = round(random.random() * 100)
    print('ESSE É O NUMERO SECRETO {}'.format(secret_number))

    while total_try > 0:
        try_number = int(input('Escolha um número entre 1 e 100: '))

        if try_number == secret_number:
            print('VOCÊ ACERTOU!!!\n')
            print('FIM DO JOGO.')
            break
        else:
            if try_number > secret_number:
                print('O número que você escolheu é MAIOR\n')
            else:
                print('O número que você escolheu é MENOR\n')

            total_try -= 1
            if total_try > 0:
                print('Você ERROU, e tem {} tentativas'.format(total_try))
            else:
                print('VOCÊ ERROU!!!\n')
                print('FIM DO JOGO.')
