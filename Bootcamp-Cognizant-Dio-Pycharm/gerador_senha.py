import random
import string


tamanho_senha = int(input('Digite o numero de caracteres que deve conter na senha: '))
lista_caracteres = string.ascii_letters + string.digits + '!@#$%&*'

senha_1 = [random.choice(lista_caracteres) for x in range(tamanho_senha)]
senha_1_join = ''.join(senha_1)

print(senha_1)
print(senha_1_join)

rnd = random.SystemRandom()
senha = [rnd.choice(lista_caracteres) for i in range(tamanho_senha)]
senha_join = ''.join(senha)

print(senha)
print(senha_join)
