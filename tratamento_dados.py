from dados import registros

def verificacao_log(email, senha):
    if email in registros:
        if registros[email]["senha"] == senha:
            return True
        else:
            print("Senha incorreta, por favor tente novamente")
            return False
    else:
        print("Email não registrado.")
        return False
    
def verificacao_reg(email, senha, c_senha):
    if ".com" not in email and "@" not in email:
        print("Email incompleto, inclua '@' e '.com'.")
        return True
    elif len(senha) < 8:
        print("Sua senha deve ter no mínimo 8 dígitos.")
        return True
    elif senha != c_senha:
        print("Senhas diferentes.")
        return True
    else: 
        return False
    

    

def log(email, senha):
    print(f"""
============ RESPOSTA ============

     !!!LOGADO COM SUCESSO!!!

==================================
""")

def reg(email, senha, c_senha):


    print(f"""
============ RESPOSTA ============

    !!!REGISTRADO COM SUCESSO!!!

==================================
""")