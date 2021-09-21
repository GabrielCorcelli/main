frase= str(input('digite uma frase:')).strip().upper()
palavras = frase.split()
junto=''.join(palavras)
inverso=''
print('você digitou a frase {}'.format(junto))
for letra in range(len(junto)-1,-1,-1):
    inverso+= junto[letra]
print(junto,inverso)
if inverso==junto:
    print("temos um palindromo")
else:
    print('a frase digitada nao é um palindromo')