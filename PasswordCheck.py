# Funció per verificar la seguretat de la contrasenya
def password_security(password):
    # Comprovem si la contrasenya té al menys 8 caràcters
    if len(password) < 8:
        return False
    # Comprovem si la contrasenya té al menys una lletra majúscula
    if not any(char.isupper() for char in password):
        return False
    return True    