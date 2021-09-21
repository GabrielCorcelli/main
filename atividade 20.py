from random import shuffle
n1=(input('primeiro aluno:'))
n2=(input('segundo aluno:'))
n3=(input('terceiro aluno:'))
lista=[n1,n2,n3]
shuffle(lista)
print('a ordem sera')
print(lista)