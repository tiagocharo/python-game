import forca
import adivinhacao

print('BEM-VINDO!')
name = input('Qual é seu nome? ').upper()
print('====================')
print('{}, ESCOLHA SEU JOGO'.format(name))
print('====================\n')

print('(1) FORCA || (2) ADIVINHAÇÃO\n')
game = int(input('Qual jogo voê escolhe? '))

if game == 1:
    forca.play()
else:
    adivinhacao.play()