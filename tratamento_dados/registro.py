from dados.dados import registros
import json

# VERIFICAÇÃO DE CREDENCIAIS CORRETAS PARA O REGISTRO NO BANCO DE DADOS
def verificacao_reg(email, senha, c_senha):
    if ".com" not in email or "@" not in email:
        print("Credencial incompleta, inclua '@' e '.com'.")
        return False
    elif len(senha) < 8:
        print("Sua senha deve ter no mínimo 8 dígitos.")
        return False
    elif senha != c_senha:
        print("Senhas diferentes.")
        return False
    else:
        updateCredenciais(email, senha)
        return True


# IMPORTANDO AS CREDENCIAIS PARA O DICIONÁRIO LOCALIZADO EM DADOS.PY
def updateCredenciais(email, senha, acesso="[NOVA] SEM ACESSO"):
        registros[email] = {"senha": senha, "acesso": acesso} 
        saveCredenciais(registros)

# SALVANDO AS CREDENCIAIS DE ACORDO COM INFORMAÇÕES PRESENTES NO BANCO DE DADOS .PY
def saveCredenciais(registros, arquivo = "credenciais.json"):
    with open(arquivo, "w") as f:
        return json.dump(registros, f)
    
# MENSAGEM DE SUCESSO
def reg():
    print(f"""
============ RESPOSTA ============

    !!!REGISTRADO COM SUCESSO!!!

==================================
""")