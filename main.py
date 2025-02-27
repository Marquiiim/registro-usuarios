from dados import registros
from tratamento_dados import verificacao_log, verificacao_reg, log, reg
from templates import menu, logar_dinamic, logar, registro_dinamic, registro


while True:

    options = input(menu).upper()

    if options == "L":
        while True:
            email = input(logar)
            senha = input(logar)
            verificacao_log(email, senha)
            if verificacao_log == False:
                break
            else:
                print("Tente novamente.\n")
        log(email, senha)

    elif options == "R":
        while True:
            email = input(registro)
            senha = input(registro)
            c_senha = input(registro)
            verificacao_reg(email, senha, c_senha)
            break
        reg(email, senha, c_senha)

    elif options == "X":
        raise SystemExit("Sistema finalizado.")

    else:
        print("Operação não encontrada, tente novamente.")