import socket
import sys


def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        print('Socket criado com sucesso!')
    except socket.error as error:
        print('Conexão falhou!')
        print(f'Error: {error}')
        sys.exit()

    host_alvo = input('Digite o Host ou IP a ser conectado: ')
    porta_alvo = int(input('Digite a porta a ser conectada: '))

    try:
        client.connect((host_alvo, porta_alvo))
        print(f'Cliente TCP conectado com sucesso no\nHost: {host_alvo}\nPorta: {porta_alvo}')
        client.shutdown(2)
    except socket.error as error:
        print(f'Conexão com o host {host_alvo} e porta {porta_alvo} falhou!')
        print(f'Error: {error}')
        sys.exit()


if __name__ == "__main__":
    main()
