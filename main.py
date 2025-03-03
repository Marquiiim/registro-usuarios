from tratamento_dados import verificacao_log, verificacao_reg, loadCredenciais, log, reg
from templates import menu, logar_dinamic, registro_dinamic


while True:

    options = input(menu).upper()

    if options == "L":
        while True:
            email = input(logar_dinamic())
            senha = input(logar_dinamic(email))
            if verificacao_log(email, senha) == True:
                print(logar_dinamic(email, senha))
                break
            else:
                print("Tente novamente.\n")
        log()

    elif options == "R":
        while True:
            email = input(registro_dinamic())
            senha = input(registro_dinamic(email))
            c_senha = input(registro_dinamic(email, senha))
            if verificacao_reg(email, senha, c_senha) == True:
                print(registro_dinamic(email, senha, c_senha))
                break
            else:
                print("Tente novamente.\n")
        reg()

    elif options == "D":
        loadCredenciais()

    elif options == "X":
        raise SystemExit("Sistema finalizado.")

    else:
        print("Operação não encontrada, tente novamente.")