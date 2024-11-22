import bcrypt

def hash_password(password: str) -> str:
    """
    Genera un hash seguro para una contraseña.
    :param password: La contraseña en texto plano.
    :return: La contraseña encriptada (hashed).
    """
    salt = bcrypt.gensalt()  # Genera una sal única
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Retorna el hash como string

def check_password(password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña coincide con un hash almacenado.
    :param password: La contraseña en texto plano.
    :param hashed_password: El hash de la contraseña almacenado.
    :return: True si coinciden, False en caso contrario.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
