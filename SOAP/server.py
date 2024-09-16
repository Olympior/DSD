from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class ExampleService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def example_method(ctx, name):
        return f"Name received: {name}"

application = Application(
    [ExampleService],
    tns='http://example.org/wsdl/',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Server is running on http://localhost:8000/?wsdl")
    server.serve_forever()
