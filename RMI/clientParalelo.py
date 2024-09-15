import Pyro5.api

def main():
    ns = Pyro5.api.locate_ns()  # Conecta ao servidor de nomes
    uri = ns.lookup("objRegisterFactory")  # Procura a fábrica de objetos
    text_processor = Pyro5.api.Proxy(uri)  # Cria um proxy para uma nova instância do objeto remoto

    # Envia um texto para o servidor
    texto = input("Digite um texto para enviar ao servidor: ")
    resposta = text_processor.process_text(texto)
    print(f"Resposta do servidor: {resposta}")

if __name__ == "__main__":
    main()
