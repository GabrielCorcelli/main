import math
co=float(input('digite o tamanho do cateto oposto:' ))
ca=float(input('digite o tamanho do cateto adjacente'))
hi=math.hypot(co,ca)
print('o valor da hipotenusa é {:.2f}'.format(hi))