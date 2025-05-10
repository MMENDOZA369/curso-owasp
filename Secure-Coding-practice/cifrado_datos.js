const crypto = require('crypto');

// Clave y vector de inicialización (IV) para el cifrado
const clave = crypto.randomBytes(32); // 256 bits
const iv = crypto.randomBytes(16); // 128 bits

// Función para cifrar datos
function cifrarDatos(datos) {
    const cipher = crypto.createCipheriv('aes-256-cbc', clave, iv);
    let cifrado = cipher.update(datos, 'utf8', 'hex');
    cifrado += cipher.final('hex');
    return cifrado;
}

// Función para descifrar datos
function descifrarDatos(cifrado) {
    const decipher = crypto.createDecipheriv('aes-256-cbc', clave, iv);
    let descifrado = decipher.update(cifrado, 'hex', 'utf8');
    descifrado += decipher.final('utf8');
    return descifrado;
}

const datos ="Informacion sensible";
const datosCifrados = cifrarDatos(datos);
console.log("Datos cifrados:", datosCifrados);

const datosDescifrados = descifrarDatos(datosCifrados);
console.log("Datos descifrados:", datosDescifrados);
// Almacenar la clave y el IV de forma segura
// (por ejemplo, en un entorno seguro o utilizando un gestor de secretos)
// Nota: En un entorno de producción, asegúrate de manejar la clave y el IV de forma segura.
// No almacenes la clave y el IV en el código fuente
// y utiliza un gestor de secretos o un entorno seguro para su almacenamiento.
// Además, considera el uso de un algoritmo de cifrado más seguro y actualizado
// y revisa las mejores prácticas de cifrado para tu caso de uso específico.
// Recuerda que el cifrado es solo una parte de la seguridad de los datos.
// Asegúrate de implementar otras medidas de seguridad adecuadas,
// como el control de acceso, la autenticación y la auditoría,
// para proteger tus datos de manera integral.