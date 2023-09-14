import re
from django.contrib import messages
from django.contrib.messages import constants

def password_is_valid(request, password, confirm_password):
    if len(password) < 6:
        messages.add_message(request, constants.ERROR, 'Senha menor que 6 caracteres não permitido')
        return False
    
    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas informadas devem ser iguais')
        return False
    
    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Senha não possui letras de a-z')
        return False
    
    return True