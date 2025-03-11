from dados.dados import registros, usuarios
import json
import shutil

# CARREGA O ARQUIVO JSON QUE CONTÉM AS CREDENCIAIS PARA A FUNÇÃO VERIFICATION_REGISTRER FAZER A ANÁLISE DO DOCUMENTO.
def load_credentials(arquivo = "credenciais.json"):
    with open(arquivo, "r") as f:
        registros = json.load(f)
    return registros

# VERIFICAÇÃO DE CREDENCIAIS CORRETAS PARA O REGISTRO NO BANCO DE DADOS
def verification_register(email, senha, c_senha):
    credenciais = load_credentials()

    if email in credenciais:
        print("[ERROR] Email já cadastrado.")
    elif ".com" not in email or "@" not in email:
        print("[ERROR] Credencial incompleta, inclua '@' e '.com'.")
        return False
    elif len(senha) < 8:
        print("[ERROR] Sua senha deve ter no mínimo 8 dígitos.")
        return False
    elif senha != c_senha:
        print("[ERROR] Senhas diferentes.")
        return False
    else:
        update_credenciais(email, senha)
        return True


# IMPORTANDO AS CREDENCIAIS PARA O DICIONÁRIO LOCALIZADO EM DADOS.PY
def update_credenciais(email, senha, acesso="[NOVA] SEM ACESSO"):
    registros[email] = {"senha": senha, "acesso": acesso}

    dados_gerais = usuarios | registros
    
    try:
        shutil.copyfile("credenciais.json", "credenciais_backup.json")
    except FileNotFoundError:
        pass

    save_credenciais(dados_gerais)
        

# SALVANDO AS CREDENCIAIS DE ACORDO COM INFORMAÇÕES PRESENTES NO BANCO DE DADOS .PY
def save_credenciais(dados_credenciais, arquivo = "credenciais.json"):
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