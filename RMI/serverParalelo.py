import Pyro5.api

@Pyro5.api.expose
class TextProcessor:
    def process_text(self, text):
        print(f"Mensagem recebida do cliente: {text}")
        return f"Servidor processou o texto: {text}"

def main():
    daemon = Pyro5.api.Daemon()  # Cria o daemon Pyro5
    ns = Pyro5.api.locate_ns()   # Conecta ao servidor de nomes
    
    # Registra a fábrica de objetos (classe) no servidor
    uri_factory = daemon.register(TextProcessor)  # Registra a classe como um criador de instâncias

    # Registrar a fábrica de objetos no servidor de nomes
    ns.register("objRegisterFactory", uri_factory)

    print(f"Servidor pronto. Fábrica de objetos registrada. URI da fábrica: {uri_factory}")
    daemon.requestLoop()  # Mantém o servidor ativo

if __name__ == "__main__":
    main()
