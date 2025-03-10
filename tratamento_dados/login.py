from dados.dados import usuarios
from datetime import datetime

# VERIFICAÇÃO PARA LOGIN E COLETA DE ACESSO PARA ADICIONAR HORÁRIO DE ACESSO
def verification_login(email, senha):
    acesso = datetime.now()
    
    if email in usuarios:
        if usuarios[email]["senha"] == senha:
            return True
        else:
            print("Senha incorreta, por favor tente novamente")
            return False
    else:
        print("Email não registrado.")
        return False

# MENSAGEM DE SUCESSO
def log():
    print(f"""
============ RESPOSTA ============

     !!!LOGADO COM SUCESSO!!!

==================================
""")