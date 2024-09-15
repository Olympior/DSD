from zeep import Client

# URL do WSDL gerado pelo servidor
wsdl = 'http://localhost:8080/AccountService?wsdl'

# Criar um cliente SOAP
client = Client(wsdl=wsdl)

# Criar uma conta
response = client.service.createAccount('JohnDoe')
print(response)

# Obter detalhes da conta
response = client.service.getAccount('12345')
print(response)