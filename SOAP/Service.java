import jakarta.jws.WebMethod;
import jakarta.jws.WebService;

@WebService
public interface Service {
    @WebMethod
    String greet(String name);
}
