import javax.servlet.http.*;

public class SessionSecure extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) {
        // Securely manage session
        HttpSession session = request.getSession(true);
        session.setMaxInactiveInterval(30 * 60); // 30 minutes
        Cookie cookie = new Cookie("JSESSIONID", session.getId());
        cookie.setHttpOnly(true); // Prevents JavaScript access
        cookie.setSecure(true); // Ensures cookie is sent over HTTPS
        response.addCookie(cookie);
        String usuario = request.getParameter("usuario");
        session.setAttribute("usuario", usuario);
    }
  
}