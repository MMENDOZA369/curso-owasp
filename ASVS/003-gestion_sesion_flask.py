from flask import Flask, session, redirect, url_for, request  # Importar Flask y módulos relacionados
from flask_session import Session  # Importar Flask-Session

app = Flask(__name__)

# Configuración de sesión segura
app.config['SESSION_TYPE'] = 'filesystem'  # Almacena la sesión en el sistema de archivos
app.config['SECRET_KEY'] = 'tu_clave_secreta'  # Cambia esto por una clave secreta segura
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Asegúrate de que la cookie de sesión solo se envíe a través de HTTPS
app.config['SESSION_COOKIE_SECURE'] = True  # Asegúrate de que la cookie de sesión solo se envíe a través de HTTPS
Session(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['usuario'] = request.form['usuario']
        return redirect(url_for('dashboard'))
    return '''
        <form method="post">
            Usuario: <input type="text" name="usuario">
            <input type="submit" value="Iniciar sesión">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return f'Bienvenido, {session["usuario"]}!'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Ejecuta la aplicación con HTTPS
# Nota: Para producción, utiliza un certificado SSL real en lugar de 'adhoc'.
# Asegúrate de que tu servidor web esté configurado para manejar HTTPS correctamente.