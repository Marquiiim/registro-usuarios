# ÁREA DE TEMPLATES VISUAIS

menu = f"""
============ MENU ============

        [L] Logar
        [R] Registrar
        [D] Dados do sistema
        [X] Sair do sistema

==============================
=>"""

def logar_dinamic(email="", senha=""):   
        logar = f"""
============ LOGAR ============

Email: {email}
Senha: {senha}

        [C] Cancelar

==============================
=>"""
        return logar

def registro_dinamic(email="", senha="", c_senha=""):
        registro = f"""
============ REGISTRO ============

        Email: {email}
        Senha: {senha}
        Repita sua senha: {c_senha}

        [C] Cancelar

==============================
=>"""
        return registro