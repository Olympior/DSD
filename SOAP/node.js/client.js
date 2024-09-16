const soap = require('soap');

// URL do WSDL gerado pelo servidor Python
const url = 'http://localhost:8000/?wsdl';

// Criação do cliente SOAP
soap.createClient(url, function(err, client) {
    if (err) throw err;

    // Dados que você quer enviar
    const args = { name: "João" };

    // Chamada ao método 'save_name' do servidor SOAP
    client.save_name(args, function(err, result) {
        if (err) throw err;

        // Resposta do servidor
        console.log('Resposta do servidor:', result);
    });
});