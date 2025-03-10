from tratamento_dados.login import verification_login, log
from tratamento_dados.registro import verification_register, reg
from tratamento_dados.admin import load_credenciais
from templates.templates import menu, logar_dinamic, registro_dinamic

def cancel_operation(prohibited):
    if prohibited.upper() == "C":
        return True
    return False

def execute_operation(operation, *args):
    while True:
        prohibited = input(operation(*args))
        if cancel_operation(prohibited):
            return None
        return prohibited
    
def process_login():
    while True:
        email = execute_operation(logar_dinamic)
        if email is None:
            break

        senha = execute_operation(logar_dinamic, email)
        if senha is None:
            break

        if verification_login(email, senha):
            print(logar_dinamic(email, senha))
            log()
            break
        else:
            print("Tente novamente.\n")

def process_register():
    while True:
        email = execute_operation(registro_dinamic)
        if email is None:
            break

        senha = execute_operation(registro_dinamic, email)
        if senha is None:
            break

        c_senha = execute_operation(registro_dinamic, email, senha)
        if c_senha is None:
            break

        if verification_register(email, senha, c_senha):
            print(registro_dinamic(email, senha, c_senha))
            reg()
            break

def close_system():
    raise SystemExit("Sistema finalizado.")

sections = {
    "L": process_login,
    "R": process_register,
    "D": load_credenciais,
    "X": close_system 
}

while True:
    options = input(menu).upper()

    action = sections.get(options, lambda: print("Operação não encontrada, tente novamente."))
    action()