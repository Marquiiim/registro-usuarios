from dados.dados import registros, usuarios
import json
import shutil

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

    dados_gerais = usuarios | registros
    
    try:
        shutil.copyfile("credenciais.json", "credenciais_backup.json")
    except FileNotFoundError:
        pass

    saveCredenciais(dados_gerais)
        

# SALVANDO AS CREDENCIAIS DE ACORDO COM INFORMAÇÕES PRESENTES NO BANCO DE DADOS .PY
def saveCredenciais(dados_credenciais, arquivo = "credenciais.json"):
    try:
        with open(arquivo, "r") as f:
            credenciais_existentes = json.load(f)
    except:
        credenciais_existentes = {}

    credenciais_existentes.update(dados_credenciais)

    with open(arquivo, "w") as f:
        json.dump(credenciais_existentes, f, indent=4)
    
# MENSAGEM DE SUCESSO
def reg():
    print(f"""
============ RESPOSTA ============

    !!!REGISTRADO COM SUCESSO!!!

==================================
""")