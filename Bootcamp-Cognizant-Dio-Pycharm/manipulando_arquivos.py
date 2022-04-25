import shutil


def manipula_arquivo(nome_arquivo, mode, texto=""):
    if mode == "a" or mode == "w":
        arquivo = open(nome_arquivo, mode)
        arquivo.write(f'{texto}\n')
        arquivo.close()
    elif mode == "r":
        arquivo = open(nome_arquivo, mode)
        print(arquivo.read())
    else:
        raise ValueError("Modo incorreto. \na: atualizar arquivo\nw: escrever/sobrescrever arquivo")


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    lista_linhas = arquivo.read().split('\n')
    dic_aluno_media = {}
    for lista in lista_linhas:
        lista_notas = lista.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = sum([int(i) for i in lista_notas]) / 4
        dic_aluno_media[aluno] = str(media)
    print(dic_aluno_media)


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '../../Desktop/Desktop')


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '../../Desktop/Desktop')


copia_arquivo("notas.txt")
