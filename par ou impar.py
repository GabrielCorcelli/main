numero= int(input('digite um numero:'))
resultado= numero % 2
if resultado == 0:
    print('o numero {} é par'.format(numero))
else:
    print('o numero {} é impar'.format(numero))