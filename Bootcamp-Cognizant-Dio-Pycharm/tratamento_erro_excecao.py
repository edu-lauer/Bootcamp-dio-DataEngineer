class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, mensagem):
        self.mensagem = mensagem


while True:
    try:
        x = int(input("Entre com um numero de 0 a 10: "))
        if x > 10:
            raise InputError("Numero digitado não pode ser maior que 10")
        if x < 0:
            raise InputError("Numero digitado não pode ser menor que 0")
        break
    except ValueError:
        print("Valor digitado precisa ser numérico")
    except InputError as ex:
        print(ex)
