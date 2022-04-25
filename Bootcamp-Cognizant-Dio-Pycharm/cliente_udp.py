import socket


cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "localhost"
porta = 5433

print('[STARTING] Iniciando Cliente...')


def send():
    while True:
        msg = input('Digite a mensagem a ser enviada: ')
        cliente.sendto(msg.encode(), (host, porta))
        if msg == "!DISCONECT":
            cliente.close()
        else:
            dados, endereco = cliente.recvfrom(4096)
            dados = dados.decode()
            print(f'[RESPOSTA] Mensagem de resposta: {dados}')


send()
