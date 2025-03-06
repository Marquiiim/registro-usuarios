from tratamento_dados.login import verificacao_log, log
from tratamento_dados.registro import verificacao_reg, reg
from tratamento_dados.admin import loadCredenciais
from templates.templates import menu, logar_dinamic, registro_dinamic


while True:

    options = input(menu).upper()

    if options == "L":
        while True:
            email = input(logar_dinamic())
            senha = input(logar_dinamic(email))
            if verificacao_log(email, senha) == True:
                print(logar_dinamic(email, senha))
                log()
                break
            else:
                print("Tente novamente.\n")

    elif options == "R":
        while True:
            email = input(registro_dinamic())
            senha = input(registro_dinamic(email))
            c_senha = input(registro_dinamic(email, senha))
            if verificacao_reg(email, senha, c_senha) == True:
                print(registro_dinamic(email, senha, c_senha))
                reg()
                break
            else:
                print("Tente novamente.\n")

    elif options == "D":
        loadCredenciais()

    elif options == "X":
        raise SystemExit("Sistema finalizado.")

    else:
        print("Operação não encontrada, tente novamente.")