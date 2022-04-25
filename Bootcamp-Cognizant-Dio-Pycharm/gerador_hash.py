import hashlib


formato = 'utf-8'
frase = input('Digite a frase que deseja encriptar: ')

menu = int(input('''MENU - Escolha o tipo de hash
            1 - MD5
            2 - SHA1
            3 - SHA256
            4 - SHA512
            Digite o numero do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(frase.encode(formato))
    print(f'O hash MD5 frase é: {resultado.hexdigest()}')
elif menu == 2:
    resultado = hashlib.sha1(frase.encode(formato))
    print(f'O hash SH1 frase é: {resultado.hexdigest()}')
elif menu == 3:
    resultado = hashlib.md5(frase.encode(formato))
    print(f'O hash MD5 frase é: {resultado.hexdigest()}')
elif menu == 4:
    resultado = hashlib.sha512(frase.encode(formato))
    print(f'O hash SHA512 frase é: {resultado.hexdigest()}')
else:
    print('Não foi selecionado um dos métodos de hash mencionado!')

