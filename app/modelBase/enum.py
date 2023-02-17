from http.client import BAD_GATEWAY, BAD_REQUEST, CONFLICT, CREATED, NOT_FOUND, OK, UNAUTHORIZED
from xmlrpc.client import INTERNAL_ERROR


class TYPECODE(object):
    SI = True
    NO = False
    ERROR_BD = "9999"
    OK = "0000"
    BAD_REQUEST = "0400"
    CONFLICT = "0409"
    UNAUTHORIZED = "0401"
    NOT_FOUND = "0404"
    CREATED = "0201"
    INTERNAL_ERROR = "0500"

class MESSAGE(object):
    DECORATOR = "por favor intente de nuevo"
    OK = "Proceso exitoso.!"
    NOT_FOUND = "No existe el recurso solicitado, "+DECORATOR+".!"
    BAD_REQUEST = "Error.!"
    INTERNAL_ERROR = "Error inesperado.!"
    CREATED = "Creación exitosa.!"
    UPDATE = "Actualización exitosa.!"
    DESTROY = "Eliminación exitosa.!"
    NULL = "null"
    BAD_CREDENTIALS = "Credenciales incorrectas.!"
    LOGIN = "Login exitoso.!"
    BAD_LOGIN = "'Usuario o contraseña no validos.!"
    NOT_SESSION = "Su cuenta ha sido dada de baja.!"
    ON_SESSION = "Ya se ha iniciado sesión con este usuario.!"
    SESSION_MESSAGE = "Sesiones de usuario eliminadas.!"
    TOKEN_MESSAGE = "Token eliminado.!"
    NOT_FOUND_USER = "Usuario no encontrado.!"
    NOT_FOUND_TOKEN = "No se ha encontrado token en le petición.!"
    UNAUTHORIZED = "No estas autorizado para acceder al recurso.!"
    SESSION_EXPIRED = "Sesión expirada.!"
    DATA_NOT_SAVE = "Los siguientes registros no pudieron ser insertados, "+DECORATOR+".!"
    DATA_NOT_UPDATE = "Los siguientes registros no pudieron ser actualizados, "+DECORATOR+".!"
    DATA_EMPTY = "No existen registros,"+DECORATOR+" uno.!"