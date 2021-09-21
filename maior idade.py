from datetime import  date
atual=date.today().year
totalmaior=0
totalmenor= 0
for pessoas in range(1,8):
    nasc= int(input('digite o ano que a {} pessoa nasceu?:'.format(pessoas)))
    idade= atual - nasc
    if idade>=18:
        totalmaior+= 1
    else:
        totalmenor+=1
print('tem {}  de maior e {} pessoas de menor'.format(totalmaior,totalmenor))
