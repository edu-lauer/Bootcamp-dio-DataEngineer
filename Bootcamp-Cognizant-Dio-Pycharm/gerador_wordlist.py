import itertools


palavra = input('Palavra a ser permutada: ')

resultado = itertools.permutations(palavra, len(palavra))

for i in resultado:
    print(''.join(i))
