# ARQUIVO PYTHON COM ALGORITMO ANTIGO DESSE SISTEMA.

"""
while True:

    options = input(menu).upper()

    if options == "L":
        while True:
            email = input(logar_dinamic())
            if email.upper() == "C":
                print("Operação Cancelada.")
                break

            senha = input(logar_dinamic(email))
            if senha.upper() == "C":
                print("Operação Cancelada.")
                break
            
            if verificacao_log(email, senha):
                print(logar_dinamic(email, senha))
                log()
                break
            else:
                print("Tente novamente.\n")

    elif options == "R":
        while True:
            email = input(registro_dinamic())
            if email.upper() == "C":
                print("Operação Cancelada.")
                break

            senha = input(registro_dinamic(email))
            if senha.upper() == "C":
                print("Operação Cancelada.")
                break
            
            c_senha = input(registro_dinamic(email, senha))
            if c_senha.upper() == "C":
                print("Operação Cancelada.")
                break
            
            if verificacao_reg(email, senha, c_senha):
                print(registro_dinamic(email, senha, c_senha))
                reg()
                break
            else:
                print("Tente novamente.\n")

    elif options == "D":
        load_credenciais()

    elif options == "X":
        raise SystemExit("Sistema finalizado.")

    else:
        print("Operação não encontrada, tente novamente.")
"""