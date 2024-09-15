import jakarta.xml.ws.Endpoint;

public class Server {
    public static void main(String[] args) {
        // Publica o serviço SOAP na URL especificada
        Endpoint.publish("http://localhost:8080/soap/MyService", new ServiceImpl());
        System.out.println("SOAP server is running at http://localhost:8080/soap/MyService?wsdl");
    }
}
