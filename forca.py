import random

def play():
    print("===================================")
    print("BEM-VINDO AO JOGO DA FORCA DE NOMES")
    print("===================================\n")

    file = open('file.txt', 'r')

    palavras = []
    for nome in file:
        nome = nome.strip()
        palavras.append(nome)

    file.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    enforcou = False
    acertou = False
    erros = 0
    tracos = [ '_' for letra in palavra_secreta]

    while not enforcou and not acertou:
        chute = input("Qual letra você escolhe? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    tracos[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == len(palavra_secreta)
        acertou = '_' not in tracos
        print(tracos)

    if acertou:
        print('VOCÊ GANHOU!!!\n')
    else:
        print('VOCÊ PERDEU!!!\n')

    print('FIM DO JOGO!!!')

if __name__ == "__main__":
    jogar()
            