nome= str(input('digite seu nome:')).strip()
print('seu nome maiusculo é {}'.format(nome.upper()))
print('seu nome minisculo é {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa= nome.split()
print(separa)
print('seu primeiro é {} e ele tem {} letras'.format(separa[0],len(separa[0])))