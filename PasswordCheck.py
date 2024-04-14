# Funció per verificar la seguretat de la contrasenya
def password_security(password):
    # Comprovem si la contrasenya té al menys 8 caràcters
    if len(password) < 8:
        return False
    return True    