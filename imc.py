peso=float(input('qual o seu peso??'))
altura=float (input('Qual a sua altura'))
imc=peso/(altura**2)
print("o imc dessa pessoa é {:.1f}".format(imc))
if imc < 18.5:
    print('você esta abaixo do peso normal')
elif imc>= 18.5 and imc<25:
    print("parabens voce esta na faixa de peso normal")
elif 25<= imc < 30:
    print('voce esta em sobrepeso')
elif 30<= imc < 40:
    print('voce esta em obesidade')
elif imc>=40:
    print('voce esta em obesidade morbida')