a = round(float(input('Entre novamente com sua nota de peso 3.5: ')), 1)
while a > 10 or a < 0:
    a = float(input('Nota inválida! Entre novamente com sua nota de peso 3.5: '))

b = round(float(input('Entre novamente com sua nota de peso 7.5: ')), 1)
while b > 10 or b < 0:
    b = float(input('Nota inválida! Entre novamente com sua nota de peso 7.5: '))

# TODO: Complete os espaços em branco com as respectivas variáveis para o cálculo da média.
media = (a * 3.5 + b * 7.5) / 11

# TODO: Complete com a variável que representa o resultado da média.
print(f'MEDIA = {media: .5f}')
