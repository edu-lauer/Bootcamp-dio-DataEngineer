import ctypes


atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetfileAttributesW('ocultar_arquivo.txt', atributo_ocultar)

if retorno:
    print('Arquivo ocultado')
else:
    print('Não foi possível ocultar o arquivo')
