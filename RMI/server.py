import Pyro5.api

#Rodando o servidor
'''python -m Pyro5.nameserver -n localhost -p 9090'''

# Definindo o objeto remoto
@Pyro5.api.expose
class TextProcessor:
    def process_text(self, text):
        print(f"Nick Recebido do client: {text}")
        return f"Olá: {text}"

# Iniciando o serviço de daemon
def main():
    # Cria um daemon Pyro5
    daemon = Pyro5.api.Daemon()

    # Registrar o objeto remoto
    text_processor = TextProcessor()

    # Localizando o servidor de nomes (porta 9090)
    ns = Pyro5.api.locate_ns(host="localhost", port=9090)
    uri = daemon.register(text_processor)

    # Registrar o objeto no servidor de nomes
    ns.register("objRegister", uri)

    print(f"Servidor pronto. URI: {uri}")

    # Mantém o servidor ativo aguardando conexões
    daemon.requestLoop()

if __name__ == "__main__":
    main()