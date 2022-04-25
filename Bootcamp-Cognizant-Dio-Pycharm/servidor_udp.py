import socket


host = 'localhost'
porta = 5433

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, porta))

mensagem = "Recebida a mensagem do cliente"

print('[STARTING] Iniciando Server....')
while True:
    dados, endereco = server.recvfrom(4096)
    dados = dados.decode()
    print(f'Mensagem recebida: {dados}')
    if dados == "!DISCONECT":
        print('Cliente desconectado do servidor')
    else:
        print('Confirmação de recebimento')
        server.sendto(mensagem.encode(), endereco)