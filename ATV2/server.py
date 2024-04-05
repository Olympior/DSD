import socket

# Configurações do servidor
HOST = '192.168.0.10'  # Endereço IP do servidor (localhost)
PORT = 12345        # Porta para comunicação

# Palavra escolhida pelo servidor
PALAVRA_SECRETA = "senha"

# Inicializa o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

# Dicionário para armazenar os nomes e endereços dos clientes
client_names = {}

# Conjunto para armazenar as letras acertadas
letras_acertadas = set()

def verificar_letra(palavra, letra):
    return letra in palavra

try:
    print(f"Servidor iniciado em {HOST}:{PORT}")
    while True:
        data, addr = server_socket.recvfrom(1024)
        if addr not in client_names:
            client_names[addr] = data.decode('utf-8')  # Registra o nome do cliente
            print(f"Conexão estabelecida com {client_names[addr]} ({addr[0]}:{addr[1]})")
            continue  # Ignora o processamento do nome do cliente
        
        letra = data.decode('utf-8').lower()
        
        if len(letra) == 1:
            if verificar_letra(PALAVRA_SECRETA, letra):
                letras_acertadas.add(letra)
                server_socket.sendto(f"A Letra: {letra} \n é uma letra certa!\n".encode('utf-8'), addr)
                
            else:
                server_socket.sendto(f"A letra {letra} não existe na palavra secreta!\n".encode('utf-8'), addr)
                
            letras_enviadas = ", ".join(sorted(letras_acertadas))  
            server_socket.sendto(f"Letras acertadas até agora: {letras_enviadas}\n".encode('utf-8'), addr)
        
        else:
            if len(letra) == len(PALAVRA_SECRETA):
                if PALAVRA_SECRETA == letra:
                    print(f"Cliente {client_names[addr]} venceu! A palavra secreta era '{PALAVRA_SECRETA}'.")
                    for client_addr in client_names:
                        server_socket.sendto(f"Cliente {client_names[addr]} venceu o jogo! A palavra secreta era '{PALAVRA_SECRETA}'.".encode('utf-8'), client_addr)
                    break   
                else: 
                    server_socket.sendto("Palavra Errada!.".encode('utf-8'), addr)
                    
            else:
                server_socket.sendto(f"Comando não recebido ou invalido.\n A palavra secreta tem {len(PALAVRA_SECRETA)} letras.\n".encode('utf-8'), addr)

except KeyboardInterrupt:
    print("Servidor encerrado.")
finally:
    server_socket.close()