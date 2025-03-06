import json

# MOSTRANDO CREDENCIAIS ARMAZENADAS NO ARQUIVO JSON
def loadCredenciais(arquivo = "credenciais.json"):
    try:
        with open(arquivo, "r") as f:
            registros = json.load(f)

            for email, info in registros.items():
                print(f"""
                    Email: {email}
                    Senha: {info["senha"]}
                    Último acesso: {info["acesso"]}
                """)
    except FileNotFoundError:
        return {}