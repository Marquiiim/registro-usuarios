from dados import registros
from tratamento_dados import verificacao_log, verificacao_reg, log, reg
from templates import menu, logar, registro


while True:
    template_menu = menu
    template_login = logar
    template_register = registro

    options = input(menu).upper()

    if options == "L":
        while True:
            email = input(logar)
            senha = input(logar)
            verificacao_log(email=email, senha=senha)
            if verificacao_log == False:
                break
            else:
                print("Tente novamente.\n")
        log(email=email, senha=senha)
        


    elif options == "R":
        while True:
            email = input(registro)
            senha = input(registro)
            c_senha = input(registro)
            verificacao_reg(email=email, senha=senha, c_senha=senha)
            break
        reg(email=email, senha=senha, c_senha=senha)

    elif options == "X":
        raise SystemExit("Sistema finalizado.")

    else:
        print("Operação não encontrada, tente novamente.")