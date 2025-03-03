from tratamento_dados import verificacao_log, verificacao_reg, log, reg
from templates import menu, logar_dinamic, logar, registro_dinamic, registro


while True:

    options = input(menu).upper()

    if options == "L":
        while True:
            email = input(logar)
            senha = input(logar)
            if verificacao_log(email, senha) == True:
                print(logar_dinamic(email, senha))
                break
            else:
                print("Tente novamente.\n")
        log()

    elif options == "R":
        while True:
            email = input(registro)
            senha = input(registro)
            c_senha = input(registro)
            if verificacao_reg(email, senha, c_senha) == True:
                print(registro_dinamic(email, senha, c_senha))
                break
            else:
                print("Tente novamente.\n")
        reg()

    elif options == "X":
        raise SystemExit("Sistema finalizado.")

    else:
        print("Operação não encontrada, tente novamente.")