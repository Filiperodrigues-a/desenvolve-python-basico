import re
def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'[0-9]', senha):
        return False
    if not re.search(r'[@#$%&]', senha):
        return False
    return True


senha = input("Escolha uma senha que tenha pelo menos 8 caracteres, pelo menos uma letra maiuscula e uma minuscula, um número e um caractere especial:")
print(validador_senha(senha))