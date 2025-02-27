menu = f"""
============ MENU ============

        [L] Logar
        [R] Registrar 
        [X] Sair do sistema

==============================
=>"""


logar = f"""
============ LOGAR ============

        Email:
        Senha:

        [C] Cancelar

==============================
=>"""

def logar_dinamic(email, senha):   
        logar = f"""
============ LOGAR ============

Email: {email}
Senha: {senha}

        [C] Cancelar

==============================
=>"""
        return logar



registro = f"""
============ REGISTRO ============

Email:
Senha:
Repita sua senha:

        [C] Cancelar

==============================
=>"""
def registro_dinamic(email, senha, c_senha):
        registro = f"""
============ REGISTRO ============

        Email: {email}
        Senha: {senha}
        Repita sua senha: {c_senha}

        [C] Cancelar

==============================
=>"""
        return registro