import jakarta.jws.WebMethod;
import jakarta.jws.WebService;

@WebService(endpointInterface = "Service")
public class ServiceImpl implements Service {
    @Override
    @WebMethod
    public String greet(String name) {
        return "Hello, " + name;
    }
}
