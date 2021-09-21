from random import randint
from time import sleep
computador= randint(0,5)
print('vou pensar em um numero entre 0 e 5 tente adivinhar qual é!')
jogador= int (input('escolha um numeor entre 0 e 5: '))
print('PROCESSANDO')
sleep(3)
if jogador == computador:
    print('parabens você ganhou')
else:
    print('voce errou,eu pensei em {} e voce colocou {}'.format(computador,jogador))
