from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class NameService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def save_name(ctx, name):
        print(f"Nome recebido: {name}")
        return f"O nome {name} foi salvo com sucesso."

# Configurando a aplicação SOAP
application = Application([NameService], 'urn:nome_service',
                          in_protocol=Soap11(), out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Servidor SOAP está rodando em http://localhost:8000")
    server.serve_forever()