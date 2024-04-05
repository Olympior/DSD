import socket

# Configurações do cliente
HOST = '192.168.0.10'  # Endereço IP do servidor (localhost)
PORT = 12345        # Porta para comunicação

# Inicializa o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    nome = input("Digite seu nome: ")  # Solicitação do nome do cliente
    client_socket.sendto(nome.encode('utf-8'), (HOST, PORT))
    
    while True:
        letra = input("Digite seu palpite: \n")
        client_socket.sendto(letra.encode('utf-8'), (HOST, PORT))
        resposta, _ = client_socket.recvfrom(1024)
        print(resposta.decode('utf-8'))
except KeyboardInterrupt:
    print("Cliente encerrado.")
finally:
    client_socket.close()
