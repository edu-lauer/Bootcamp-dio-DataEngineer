import hashlib


arquivo1 = 'notas.txt'
arquivo2 = 'notas2.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'{arquivo1} é diferente do {arquivo2}')
    print(f'{arquivo1} possui o seguinte hash: {hash1.hexdigest()}')
    print(f'{arquivo2} possui o seguinte hash: {hash1.hexdigest()}')
else:
    print(f'{arquivo1} é igual ao {arquivo2}')
    print(f'{arquivo1} possui o seguinte hash: {hash1.hexdigest()}')
    print(f'{arquivo2} possui o seguinte hash: {hash1.hexdigest()}')
