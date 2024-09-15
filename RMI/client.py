import Pyro5.api

def main():
    # Localizando o servidor de nomes na porta 9090
    ns = Pyro5.api.locate_ns(host="localhost", port=9090)

    # Encontrando o objeto pelo nome registrado no servidor
    uri = ns.lookup("objRegister")

    # Criando um proxy para o objeto remoto
    text_processor = Pyro5.api.Proxy(uri)

    # Envia um texto para o servidor
    texto = input("Diga seu Nick para o servidor: ")
    resposta = text_processor.process_text(texto)
    print(f"Resposta do servidor: {resposta}")

if __name__ == "__main__":
    main()