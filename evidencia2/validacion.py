import re

def validar_email(email):
    """Valida el formato de un correo electrónico usando regex."""
    regex = r'^\S+@\S+\.\S+$'
    return re.match(regex, email) is not None

def validar_clave(clave):
    """Valida que la contraseña cumpla con las condiciones especificadas."""
    if len(clave) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    if not any(c.islower() for c in clave):
        print("La contraseña debe tener al menos una letra minúscula.")
        return False
    if not any(c.isupper() for c in clave):
        print("La contraseña debe tener al menos una letra mayúscula.")
        return False
    if not any(c.isdigit() for c in clave):
        print("La contraseña debe tener al menos un número.")
        return False
    if not any(not c.isalnum() for c in clave):
        print("La contraseña debe tener al menos un carácter especial.")
        return False
    return True

def validar_usuario(username):
    """Valida que el nombre de usuario esté entre 6 y 12 caracteres y no contenga caracteres especiales."""
    if 6 <= len(username) <= 12 and username.isalnum():
        return True
    print("El nombre de usuario debe tener entre 6 y 12 caracteres y no contener caracteres especiales.")
    return False
